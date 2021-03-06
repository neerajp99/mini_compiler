from src import lexer
# Create a parser to parse the lexer output


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def _utilise(self, token_type):
        """Method to utilise the current token and assign the next token to the current token"""
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Method to parse the factor"""
        token = self.current_token
        if token.token_type == 'LPAREN':
            self._utilise('LPAREN')
            paren_node = self.expr()
            self._utilise('RPAREN')
            return paren_node
        if token.token_type == 'INTEGER':
            self._utilise('INTEGER')
            return Number(token)
        elif token.token_type == 'FLOAT':
            self._utilise('FLOAT')
            return Number(token)
        elif token.token_type == 'MINUS':
            self._utilise('MINUS')
            return UnaryOperator(
                op_token=token,
                right=self.factor()
            )
        elif token.token_type == 'PLUS':
            self._utilise('PLUS')
            return UnaryOperator(
                op_token=token,
                right=self.factor()
            )
        else:
            self.error()

    def term(self):
        """Method to parse the term"""
        left_node = self.factor()
        while self.current_token.token_type in ('MUL', 'TT_DIV'):
            token = self.current_token
            if token.token_type == 'MUL':
                self._utilise('MUL')
            elif token.token_type == 'TT_DIV':
                self._utilise('TT_DIV')

            left_node = BinOperator(
                left=left_node,
                op_token=token,
                right=self.factor()
            )

        return left_node

    def expr(self):
        """Method to parse the expression"""
        left_node = self.term()

        while self.current_token.token_type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.token_type == 'PLUS':
                self._utilise('PLUS')
            elif token.token_type == 'MINUS':
                self._utilise('MINUS')

            left_node = BinOperator(
                left=left_node,
                op_token=token,
                right=self.term()
            )

        return left_node

    def print_ast(self):
        """Method to print the AST"""
        return self.expr()


class Number:
    def __init__(self, token):
        self.value = token.value

    def __str__(self):
        return f'{self.value}'


class BinOperator:
    def __init__(self, left, op_token, right):
        self.left = left
        self.op_token = op_token
        self.right = right

    def __str__(self):
        return f'({self.left}, {self.op_token}, {self.right})'


class UnaryOperator:
    def __init__(self, op_token, right):
        self.op_token = op_token
        self.right = right

    def __str__(self):
        return f'({self.op_token}, {self.right})'


# x = lexer.Lexer('-2.8 + 3 * (10 + 10)')
# y = Parser(x)
# print(y.print_ast())
# print(y)
