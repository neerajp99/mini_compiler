import re
# Create a method to generate lexer for the language


class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.lexer = {
            # Define the lexer
            'FLOAT': r'\d*\.\d+',
            'INTEGER': r'[0-9]+',
            'PLUS': r'\+',
            'MINUS': r'\-',
            'MUL': r'\*',
            'DIV': r'\/',
            'LPAREN': r'\(',
            'RPAREN': r'\)',
            'WS': r'[ \t]+',
            'NEWLINE': r'\n',
            'EOF': r'\Z',
        }
        self.tokens = (
            'FLOAT',
            'INTEGER',
            'PLUS',
            'MINUS',
            'MUL',
            'DIV',
            'LPAREN',
            'RPAREN',
            'WS',
            'NEWLINE',
            'EOF'
        )

    def error(self):
        raise Exception('Invalid token')

    def lexer_generation(self):
        # Define the regex
        regex = '|'.join('(?P<%s>%s)' %
                         (token, self.lexer[token]) for token in self.tokens)
        # Define the tokenizer
        token_regex = re.compile(regex)
        for m in token_regex.finditer(self.input_string):
            token_type = m.lastgroup
            token_value = m.group()
            if token_type == 'WS':
                continue
            if token_type == 'NEWLINE':
                yield ('NEWLINE', token_value)
            else:
                yield (token_type, token_value)
        yield ('EOF', None)


x = Lexer('+2.8 + 3 * (10 & 10)')
print(list(x.lexer_generation()))
