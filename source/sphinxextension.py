from sphinx.util.docutils import SphinxRole, SphinxDirective

from myst_parser.mocking import MockState

from docutils import nodes

class PlaceholderRole(SphinxRole):
    def run(self):
        node = nodes.inline(text=f'[{self.text}]')
        return [placeholder_node('', node)], []

class placeholder_node(nodes.General, nodes.Element):
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

def visit_placeholder_node(self, node):
    self.body.append(f'<span class="placeholder">')

def depart_placeholder_node(self, node):
    self.body.append('</span>')

def setup(app):
    app.add_role('ph', PlaceholderRole())
    app.add_directive('rewrite-rule', RewriteDirective)
    app.add_node(
        rewrite_node,
        html=(visit_rewrite_node, depart_rewrite_node),
    )

    app.add_node(
        placeholder_node,
        html=(visit_placeholder_node, depart_placeholder_node),
    )

    app.add_node(
        rewrite_seq_node,
        html=(visit_rewrite_seq_node, depart_rewrite_seq_node),
    )


    return {
        'version': '0.1',
        'env_version': 2,
        'parallel_read_safe': True,
    }
