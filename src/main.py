from src import lexer, parser, interpreter, sym_table
import sys
if __name__ == "__main__":
    input_string = input("DebLang>> ")
    lexers = lexer.Lexer(input_string)
    lexers_list = []
    print("------------------- LEXER TOKENS ------------------- \n")
    # print(lexers.print_tokens())
    symbTable = sym_table.SymbolTable()
    while lexers.has_token():
        token = lexers.get_next_token()
        print(token)
        symbTable.insert(token.value, token.token_type,
                         sys.getsizeof(token.value), 'global')
        lexers_list.append(token)
    print('\n')
    print("------------------- PARSER SYMBOL TABLE ------------------- \n")
    # symbol_table = sym_table.SymbolTable()
    print(symbTable)
    print('\n')
    parsers = parser.Parser(lexer.Lexer(input_string))
    print("------------------- PARSER AST ------------------- \n")
    print(parsers.print_ast())
    print('\n')
    print("------------------- PARSER INTERPRETER ------------------- \n")
    output = interpreter.Interpreter(parser.Parser(lexer.Lexer(input_string)))
    print(output.interpret())
