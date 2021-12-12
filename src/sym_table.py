# Create a symbol table for the compiler using parse tree
class SymbolHelper:
    def __init__(self, name, type, size, scope):
        self.name = name
        self.type = type
        self.size = size
        self.scope = scope
        self.next = None

    def __str__(self):
        return '{}\t\t {} \t\t {} \t\t {}'.format(self.name, self.type, self.size, self.scope)

    def __repr__(self):
        return '{}\t\t {} \t\t {} \t\t {}'.format(self.name, self.type, self.size, self.scope)


class SymbolTable:
    def __init__(self):
        """Constructor for the symbol table"""
        self.head = None
        self.tail = None
        self.size = 0
        # self.lexers = lexers

    def __str__(self):
        """Method to print the symbol table"""
        if self.size == 0:
            return 'Symbol table is empty'
        else:
            string = 'Symbol Table:\n ID \t\t TYPE \t\t SIZE \t\t SCOPE\n'
            current_node = self.head
            while current_node:
                string += str(current_node) + '\n'
                current_node = current_node.next
            return string

    def insert(self, name, type, size, scope):
        """Method to insert a new node in the symbol table"""
        if self.size == 0:
            self.head = SymbolHelper(name, type, size, scope)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = SymbolHelper(name, type, size, scope)
            self.tail = self.tail.next
            self.size += 1
