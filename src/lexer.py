import re
# Create a lexer class for the language
class Lexer:
    """Lexer class"""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.INTEGER = 'INTEGER'
        self.PLUS = 'PLUS'
        self.MINUS = 'MINUS'
        self.MUL = 'MUL'
        self.TT_DIV = 'TT_DIV'
        self.LPAREN = 'LPAREN'
        self.RPAREN = 'RPAREN'
        self.EOF = 'EOF'
        self.FLOAT = 'FLOAT'

    def error(self):
        raise Exception('Invalid character')

    def _scan(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self._scan()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        _count = 0
        while self.current_char is not None and self.current_char.isdigit() or self.current_char == '.':
            if self.current_char == '.':
                if _count == 1: 
                    break 
                _count = _count + 1 
                result += '.'
            else:
                
                result += self.current_char
            self._scan()
        # Check the result is a valid integer
        try:
            if '.' in result:
                return Token(self.FLOAT, float(result))
            else:
                return Token(self.INTEGER, int(result))
        except ValueError:
            self.error()
    
    def has_token(self):
        return self.current_char is not None

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()

            if self.current_char == '+':
                self._scan()
                return Token(self.PLUS, '+')

            if self.current_char == '-':
                self._scan()
                return Token(self.MINUS, '-')

            if self.current_char == '*':
                self._scan()
                return Token(self.MUL, '*')

            if self.current_char == '/':
                self._scan()
                return Token(self.TT_DIV, '/')

            if self.current_char == '(':
                self._scan()
                return Token(self.LPAREN, '(')

            if self.current_char == ')':
                self._scan()
                return Token(self.RPAREN, ')')

            self.error()

        return Token(self.EOF, None)

# Create the tokens class 
class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.token_type,
            value=repr(self.value)
        )

# x = Lexer('2.7 + 3 * (4 + 5)')
# while x.has_token():
#     print(x.get_next_token())