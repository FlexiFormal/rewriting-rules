from sphinx.util.docutils import SphinxRole, SphinxDirective

from myst_parser.mocking import MockState

from docutils import nodes

from pygments.lexer import RegexLexer
from pygments.token import Punctuation, Whitespace, Name, Operator, String
from pygments.lexers._mapping import LEXERS

__all__ = ['NbnfLexer']

LEXERS['NbnfLexer'] = (__name__, 'NBNF', ('nbnf',), ('*.nbnf',), ('text/nbnf',))


class NbnfLexer(RegexLexer):
    name = 'NBNF'
    aliases = ['nbnf']
    filenames = ['*.nbnf']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'[{}[]()]', Punctuation),
            (r'::=|:=|=|<-|->|\*|\+|\|', Operator),
            (r'''('[^']*')|("[^"]*")''', String),
            (r'<<?[a-zA-Z0-9_-]*>?>', Name),
            (r'...', Name),
        ]
    }


class PlaceholderRole(SphinxRole):
    def run(self):
        text = self.text.split('_')
        r = [nodes.Text(text[0])]
        for i in range(1, len(text)):
            r.append(nodes.subscript(text=text[i][0]))
            if len(text[i]) > 1:
                r.append(nodes.Text(text[i][1:]))
        node = nodes.inline('', *r)
        return [placeholder_node('', node)], []

class placeholder_node(nodes.General, nodes.Element):
    ...

class CategoryRole(SphinxRole):
    def run(self):
        node = nodes.inline(text=f'{self.text}')
        return [catnode('', node)], []

class catnode(nodes.General, nodes.Element):
    ...

class NlRole(SphinxRole):
    def run(self):
        r = []
        for i, s in enumerate(self.text.split('$')):
            if i % 2:
                r.append(my_math('\\(' + s + '\\)'))
            else:
                r.append(nodes.Text(s))
        node = nodes.inline('', *r)
        return [nl_node('', node)], []

class my_math(nodes.General, nodes.Element):
    def __init__(self, formula):
        super().__init__()
        self.formula = formula

class nl_node(nodes.General, nodes.Element):
    ...

class rewrite_node(nodes.General, nodes.Element):
    is_consequent = False

class rewrite_seq_node(nodes.General, nodes.Element):
    pass

class RewriteDirective(SphinxDirective):
    required_arguments = 0
    has_content = True

    def run(self):
        assert isinstance(self.state, MockState)

        node = nodes.Element()

        self.state.nested_parse(self.content, self.content_offset, node)

        children = [
                rewrite_node('', *child.children)
                if isinstance(child, nodes.paragraph) else
                rewrite_node('', child)
                for child in node.children
                ]
        if children:
            children[-1].is_consequent = True
        return [rewrite_seq_node('', *children)]
        # return children


def visit_rewrite_node(self, node):
    # style = 'text-align: center; padding: 0.5em; width: 100%; display: inline-block;'
    if node.is_consequent:
        # style += 'border-bottom: 1px solid black;'
        self.body.append(f'<hr class="rewrite-rule-separator"/>')
    self.body.append(f'<div class="rewrite-line">')

def depart_rewrite_node(self, node):
    self.body.append('</div>')

def visit_rewrite_seq_node(self, node):
    self.body.append('<div class="rewrite-rule-container">')

def depart_rewrite_seq_node(self, node):
    self.body.append('</div>')

def visit_depart_span(class_):
    def visit_node(self, node):
        self.body.append(f'<span class="{class_}">')

    def depart_node(self, node):
        self.body.append('</span>')

    return visit_node, depart_node

def visit_mymath_node(self, node):
    self.body.append(f'<span class="math notranslate nohighlight">')
    self.body.append(node.formula)

def depart_mymath_node(self, node):
    self.body.append('</span>')


def setup(app):
    app.add_role('ph', PlaceholderRole())
    app.add_role('cat', CategoryRole())
    app.add_role('nl', NlRole())
    app.add_directive('rewrite-rule', RewriteDirective)
    app.add_node(
        rewrite_node,
        html=(visit_rewrite_node, depart_rewrite_node),
    )

    app.add_node(placeholder_node, html=visit_depart_span('placeholder'))
    app.add_node(catnode, html=visit_depart_span('category'))
    app.add_node(nl_node, html=visit_depart_span('nl'))
    app.add_node(my_math, html=(visit_mymath_node, depart_mymath_node))

    app.add_node(
        rewrite_seq_node,
        html=(visit_rewrite_seq_node, depart_rewrite_seq_node),
    )


    return {
        'version': '0.1',
        'env_version': 2,
        'parallel_read_safe': True,
    }
