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
            (r'[a-zA-Z0-9_-][a-zA-Z0-9_-\']*', String),
            (r'<<?[a-zA-Z0-9_-]*>?>', Name),
            (r'...', Name),
            (r':[a-zA-Z0-9_-]+:', Name),   # placeholders
        ]
    }

def setup(app):
    """Sphinx likes having a setup function"""
