import os
from parser import *
from semantic import *


def main():
    prog = read_file('resources/input_program.txt')
    g = PascalGrammar()
    prog = g.parse(prog)
    print(*prog.tree, sep=os.linesep)
    symb_table_builder = SemanticAnalyzer()
    symb_table_builder.visit(prog)


def write_file(file_path, content):
    f = open(file_path, "w")
    f.write(content)
    f.close()


def read_file(file_path) -> str:
    f = open(file_path, "r")
    return f.read()


if __name__ == "__main__":
    main()
