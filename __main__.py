from nuts_parser import (NutsParser, Lexer)
from compiler import (Compiler)

input_str = """
loop (let i = 0) for (i < 4)(i + 1) {
    2 - 4;
}
"""

lexer = Lexer(input_str)
parser = NutsParser(lexer)

print("===================================================")

ast = parser.parse_program()

for statement in ast.statements:
    print(statement)
    print("===================================================")

print(Compiler.compile(ast))
