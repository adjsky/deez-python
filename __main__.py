from nuts_parser import (NutsParser, Lexer)
from compiler import (Compiler)

input_str = """
loop (let i = 123123) for (i < 4)(i + 1) {
    let variable = 5;
    variable + 4;
    i + 2;
}
"""

lexer = Lexer(input_str)
parser = NutsParser(lexer)

print("===================================================")

ast = parser.parse_program()

for statement in ast.statements:
    print(statement)
    print("===================================================")

compiler = Compiler(ast)

print(compiler.compile())
