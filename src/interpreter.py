from src import parser, lexer
# Create an interpreter for the language


class Number:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class AddValues:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return Number(self.left.value + self.right.value)

    def __str__(self):
        return "({} + {})".format(self.left, self.right)

    def __repr__(self):
        return str(self)


class MinusValues:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return Number(self.left.value - self.right.value)

    def __str__(self):
        return "({} - {})".format(self.left, self.right)

    def __repr__(self):
        return str(self)


class MulValues:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return Number(self.left.value * self.right.value)

    def __str__(self):
        return "({} * {})".format(self.left, self.right)

    def __repr__(self):
        return str(self)


class DivValues:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return Number(self.left.value / self.right.value)

    def __str__(self):
        return "({} / {})".format(self.left, self.right)

    def __repr__(self):
        return str(self)


class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        """ Method to interpret the program
        """
        tree = self.parser.expr()
        return self.visit(tree)

    def visit(self, node):
        """Visit a node in the AST
        """
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, self.no_visit_method)
        # print(method.__name__)
        return method(node)

    def visit_BinOperator(self, node):
        """Visit a binary operator node"""
        # self.visit(node.left)
        # self.visit(node.right)
        if node.op_token.token_type == 'PLUS':
            value = AddValues(self.visit(
                node.left), self.visit(node.right))
            op_value = value.evaluate()
            return op_value
        elif node.op_token.token_type == 'MINUS':
            value = MinusValues(self.visit(
                node.left), self.visit(node.right))
            op_value = value.evaluate()
            return op_value
        elif node.op_token.token_type == 'MUL':
            value = MulValues(self.visit(
                node.left), self.visit(node.right))
            op_value = value.evaluate()
            return op_value
        elif node.op_token.token_type == 'DIV':
            value = DivValues(self.visit(
                node.left), self.visit(node.right))
            op_value = value.evaluate()
            return op_value
        else:
            raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_UnaryOperator(self, node):
        """Visit a unary operator node and update the signs"""
        if node.op_token.token_type == 'MINUS':
            return Number(-node.right.value)
        elif node.op_token.token_type == 'PLUS':
            return Number(node.right.value)
        else:
            raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_Number(self, node):
        """Visit a number node"""
        return Number(node.value)

    def no_visit_method(self, node):
        """Method to handle nodes that have no visit method"""
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_Program(self, node):
        """Visit a program node"""
        for declaration in node.declarations:
            self.visit(declaration)


x = Interpreter(parser.Parser(lexer.Lexer('+2.8 + 3 * (10 + 10)')))
print(x.interpret())
