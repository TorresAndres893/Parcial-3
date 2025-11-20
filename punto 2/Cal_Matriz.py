from antlr4 import FileStream, CommonTokenStream
from Gramatica_matricesLexer import Gramatica_matricesLexer
from Gramatica_matricesParser import Gramatica_matricesParser
from Visitor import ExecVisitor

def main():
    input_stream = FileStream("input.txt", encoding="utf-8")
    lexer = Gramatica_matricesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Gramatica_matricesParser(stream)
    tree = parser.program()
    visitor = ExecVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)


if __name__ == "__main__":
    main()
