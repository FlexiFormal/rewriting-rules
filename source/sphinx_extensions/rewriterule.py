import re
from pathlib import Path

from docutils import nodes
from pygments import highlight
from pygments.formatters import HtmlFormatter
from sphinx.util.docutils import SphinxDirective

import latex2mathml.converter

import sys

sys.path.append(str(Path(__file__).parent))

import nbnf

def escape_html(s: str) -> str:
        return (
            s.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
        )

class RewriteRenderer:
    def __init__(self):
        self.buffer: list[str] = []

    def render_rewriterule_html(self, source):
        """ we ignore the docutils infrastructure and do our own rendering from scratch """

        w = self.buffer.append

        w('<div class="rewrite-rule-container">')

        # declarations come first, afterwards we can identify lines
        in_declarations: bool = True

        # TODO: support multi-line preconditions/nl
        for line in source.split('\n'):
            if line.startswith('|-'):
                in_declarations = False
                self.render_precondition(line)
            elif line.startswith('"'):
                in_declarations = False
                self.render_nl(line, True)
            elif line.startswith(':'):
                in_declarations = False
                self.render_nl(line, False)
            elif line.startswith('-'):
                in_declarations = False
                self.render_delimiter(line)
            elif not line.strip():  # empty line
                continue
            elif in_declarations:
                self.render_declaration(line)
            else:
                raise ValueError(f"Cannot classify line in rewrite rule: {line}")

        w('</div>')

    # ---------------------------
    # | LINE RENDERERS
    # ---------------------------

    def render_declaration(self, declaration: str):
        w = self.buffer.append
        phs, _, rest = declaration.partition(' : ')
        regex, _, examples = rest.partition('=')
        w('<div class="rewrite-line">')
        self.render_with_styled_placeholders(phs.strip(), no_colons=True)
        w(' : ')
        # w('<code>' + escape_html(regex.strip()) + '</code>')
        w('<code class="highlight">')
        self.render_with_styled_placeholders(
            highlight(regex.strip(), nbnf.NbnfLexer(), HtmlFormatter(nowrap=True)).strip()
        )
        w('</code>')
        if examples.strip():
            w(' = ')
            self.render_nl_core(examples.strip())
        w('</div>')

    def render_precondition(self, precondition: str):
        w = self.buffer.append
        assert precondition.startswith('|-')
        w('<div class="rewrite-line">')
        w('<span class="precondition-symbol">⊢</span>')
        self.render_nl_core(precondition[2:])
        w('</div>')

    def render_nl(self, nl: str, in_quotes: bool):
        w = self.buffer.append
        if in_quotes:
            if not nl.startswith('"') and nl.endswith('"'):
                raise ValueError(f"Malformed NL line: {nl}")
            nl = nl[1:-1].strip()
        w(f'<div class="rewrite-line">')
        self.render_nl_core(nl)
        w('</div>')


    def render_delimiter(self, delimiter: str):
        w = self.buffer.append
        # w('<hr class="rewrite-rule-separator"/>')
        w('<div class="divider-wrapper">')
        w('<div class="divider-line"></div>')
        w('<div class="divider-label">')
        w('<div style="width: 100em;">')
        # w(escape_html(delimiter.lstrip('-').strip()).replace(' ', '&nbsp;') or '&nbsp;')
        w(escape_html(delimiter.lstrip('-').strip()) or '&nbsp;')
        w('</div>')
        w('</div>')
        w('</div>')

    # ---------------------------
    # | LOW-LEVEL RENDERERS
    # ---------------------------

    def render_nl_core(self, content: str):
        for counter, part in enumerate(content.split('$')):
            is_formula = bool(counter % 2)
            if is_formula:
                self.render_with_styled_placeholders(
                    latex2mathml.converter.convert(
                        re.sub(
                            ':[a-zA-Z0-9_-]+:',
                            '\\\\text{\\g<0>}',
                            part
                        )
                    )
                )
            else:
                for sub_counter, subpart in enumerate(part.split('@')):
                    is_regex = bool(sub_counter % 2)
                    if is_regex:
                        w = self.buffer.append
                        w('<code class="highlight">')
                        self.render_with_styled_placeholders(
                            highlight(subpart.strip(), nbnf.NbnfLexer(), HtmlFormatter(nowrap=True)).strip()
                        )
                        w('</code>')
                    else:
                        self.render_with_styled_placeholders(escape_html(subpart))

    def render_with_styled_placeholders(self, content: str, no_colons: bool = False):
        w = self.buffer.append
        colon = '' if no_colons else ':'

        next_start = 0
        for match in re.finditer(colon + r'[a-zA-Z0-9_-]+' + colon, content):
            start, end = match.span()
            w(content[next_start:start])
            self.render_placeholder(content[start + len(colon):end - len(colon)])
            next_start = end

        w(content[next_start:])

    def render_placeholder(self, placeholder: str):
        w = self.buffer.append
        if placeholder.count('_') == 1:
            parts = placeholder.split('_')
            w(f'<span class="placeholder">{parts[0]}<sub>{parts[1]}</sub></span>')
        else:
            w(f'<span class="placeholder">{placeholder}</span>')



class rewriterule_node(nodes.General, nodes.Element):
    def __init__(self, stringcontent):
        super().__init__()
        self.stringcontent = stringcontent


class RewriteDirective(SphinxDirective):
    required_arguments = 0
    has_content = True

    def run(self):
        return [rewriterule_node('\n'.join(self.content))]

def visit_rewrite_node(self, node):
    rr = RewriteRenderer()
    rr.render_rewriterule_html(node.stringcontent)
    self.body.append(''.join(rr.buffer))

def depart_rewrite_node(self, node):
    pass


def setup(app):
    app.add_directive('rewrite-rule', RewriteDirective)
    app.add_node(
        rewriterule_node,
        html=(visit_rewrite_node, depart_rewrite_node),
    )


    return {
        'version': '0.1',
        'env_version': 2,
        'parallel_read_safe': True,
    }
