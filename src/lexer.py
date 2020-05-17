from ply import lex
import sys


QUOTE = r'(\'|")'

tokens = (
    # assignment
    'IDENTIFIER', 'ASSIGNMENT', 'SEMICOLON', 'COLON', 'COMMA',

    # main
    'PROGRAM', 'DOT',

    # blocks
    'VAR', 'BEGIN', 'END',

    # control flow
    'IF', 'THEN', 'ELSE', 'FOR', 'WHILE', 'REPEAT', 'UNTIL', 'DO', 'TO', 'DOWNTO',

    # logic
    'AND', 'OR', 'NOT',

    # operations
    'PLUS', 'MINUS', 'TIMES', 'DIVISION', 'DIV', 'MOD',

    # comparations
    'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE',

    # functions
    'LPAREN', 'RPAREN', 'PROCEDURE', 'FUNCTION',

    # types
	'REAL',	'INTEGER', 'STRING', 'CHAR',

    # types names
    'TREAL', 'TINTEGER', 'TSTRING', 'TCHAR',

    'LBRACKET', 'RBRACKET', 'RANGE', 'ARRAY', 'OF', 'SET'
)

t_DOT = r"\."
t_ASSIGNMENT = r":="
t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA = r","
t_RANGE = r"\.\."

t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVISION = r"/"

t_EQ = r"\="
t_NEQ = r"\<\>"
t_LT = r"\<"
t_GT = r"\>"
t_LTE = r"\<\="
t_GTE = r"\>\="

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"

t_REAL = r"(\-)*[0-9]+\.[0-9]+"
t_INTEGER = r"(\-)*[0-9]+"

keywords = {
    'program': 'PROGRAM', 'var': 'VAR', 'begin': 'BEGIN', 'end': 'END',

    'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'for': 'FOR',
    'while': 'WHILE', 'repeat': 'REPEAT', 'do': 'DO', 'to': 'TO',
    'downto': 'DOWNTO', 'until': 'UNTIL',

    'and': 'AND', 'or': 'OR', 'not': 'NOT',

    'div': 'DIV', 'mod': 'MOD',

    'procedure': 'PROCEDURE', 'function': 'FUNCTION',

    'real': 'TREAL', 'integer': 'TINTEGER', 'string': 'TSTRING', 'char': 'TCHAR',

    'array':'ARRAY', 'of':'OF', 'set':'SET'
}

t_ignore = ' \t'


def t_IDENTIFIER(t):
    r"[a-zA-Z]([a-zA-Z0-9])*"
    if t.value.lower() in keywords:
        t.type = keywords[t.value.lower()]

    return t


def t_CHAR(t):
    r"(\'([^\\\'])\')|(\"([^\\\"])\")"
    return t


def t_STRING(t):
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    escaped = 0
    str = t.value[1:-1]
    new_str = ""
    for i in range(0, len(str)):
        c = str[i]
        if escaped:
            if c == "n":
                c = "\n"
            elif c == "t":
                c = "\t"
            new_str += c
            escaped = 0
        else:
            if c == "\\":
                escaped = 1
            else:
                new_str += c
    t.value = new_str
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])


if __name__ == "__main__":
    lex.lex()
    test_program = 'tests/simple_test.p'
    with open(test_program) as f:
        data = f.read()
    lex.input(data)

    while True:
        token = lex.token()
        if not token:
            break
        print(token)
