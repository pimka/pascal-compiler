from ply import lex, yacc
from lexer import *
from semantic import *
from rules import *

if __name__ == "__main__":
    yacc.yacc(debug=False)

    test_program = 'tests/simple_test.p'
    with open(test_program) as f:
        data = f.read()

    ast = yacc.parse(data, lexer=lex.lex(nowarn=1))
    print()
