from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ['ZnoLexer']

class ZnoLexer(RegexLexer):
    name = 'ZnO'
    aliases = ['Zno', 'zno']
    filenames = ['*.zno']

    tokens = {
        'root': [
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),

            (r"'\\.'", String.Char),
            (r"'.'", String.Char),
            (r'"', String.Double, 'string'),

            (r"namespace", Keyword.Namespace),
            (r"module", Keyword.Namespace),
            (r"(?<=namespace)\s+[\w(::)]+", Name.Namespace),
            (r"(?<=module)\s+[\w(::)]+", Name.Namespace),

            (r"let", Keyword.Declaration),
            (r"(?<=let)\s+\w+", Name.Variable),

            (r"struct", Keyword.Declaration),
            (r"(?<=struct)\s+\w+", Name.Class),

            (r"interface", Keyword.Declaration),
            (r"(?<=interface)\s+\w+", Name.Class),

            (r"func", Keyword),
            (r"new\s*(?=(<.*>)?\()", Name.Function.Magic),
            (r"destroy\s*(?=(<.*>)?\()", Name.Function.Magic),
            (r"\w+\s*(?=(<.*>)?\()", Name.Function),
            (r"self", Name.Builtin.Pseudo),
            (r"(?<=->)\s+\w+", Name.Class),

            (r"<", Text, 'type_parameters'),
            (r"[A-Z]\w+", Name.Class),
            (r"(?<=:)\s*\w+", Name.Class),

            (r"\d+\.\d+f\d+", Number.Float.Long),
            (r"\d+\.\d+", Number.Float),
            (r"\d+[ui]\d+", Number.Integer.Long),
            (r"\d+", Number.Integer),

            (r"uses", Keyword.Namespace),
            (r"type", Keyword),

            (r"return", Keyword),
            (r"if", Keyword),
            (r"else", Keyword),
            (r"for", Keyword),
            (r"in", Keyword),

            (r"is", Operator),

            (r'[a-z_][a-z_0-9A-Z]*', Name.Variable),
            (r'.', Text),
        ],

        'type_parameters': [
            (r'>', Text, '#pop'),
            (r'\w+', Name.Class),
            (r'\s+', Text),
            (r',', Text),
        ],

        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
        ],

        'string': [
            (r'\\.', String.Escape),
            (r'[^"]', String.Double),
            (r'"', String.Double, '#pop'),
        ],
    }
