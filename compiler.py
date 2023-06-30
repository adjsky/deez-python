import nuts_ast as ast


class Compiler:
    def __init__(self, ast: ast.Program) -> None:
        self.ast = ast

    def compile(self):
        program = "int main() {{\n{compiled}\n\n\treturn 0;\n}}"

        compiled = ""

        for statement in self.ast.statements:
            compiled += self.compile_statement(statement)

        return program.format(compiled=compiled)

    def compile_statement(self, statement: ast.Statement):
        match statement:
            case ast.LoopStatement():
                return self.compile_loop_expression(statement)
            case _:
                raise NotImplementedError

    def compile_loop_expression(self, node: ast.LoopStatement):
        iteration_variable = node.init.name.value

        init = self.compile_let_statement(node.init)

        condition = self.compile_expression(node.condition)

        iter = "{} = {}".format(
            iteration_variable, self.compile_expression(node.iter.expression))

        body = ""
        for statement in node.consequence.statements:
            compiled = ""

            match statement:
                case ast.LetStatement():
                    compiled = self.compile_let_statement(statement)
                case ast.ExpressionStatement():
                    compiled = self.compile_expression(statement.expression)
                case _:
                    raise NotImplementedError

            body += "\t\t{};\n".format(compiled)

        loop = "\tfor ({init}; {condition}; {iter}) {{\n{body}\t}}".format(
            init=init, condition=condition, iter=iter, body=body)

        return loop

    def compile_let_statement(self, node: ast.LetStatement):
        # Hardcode `int` type because only `IntegerLiteral` is supported
        return "int {} = {}".format(
            node.name.value, node.value.value)

    def compile_expression(self, node: ast.Expression):
        return "{} {} {}".format(node.left.value, node.operator, node.right.value)


__all__ = ["Compiler"]
