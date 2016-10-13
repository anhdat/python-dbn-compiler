from lexer import lexer
from parser import parser
from transformer import transformer
from generator import matplot_generator


def main():
    with open('input.dbn') as f:
        def compile(input):
            return matplot_generator(transformer(parser(lexer(input))))

        input = f.read()
        matplot_code = compile(input)
        print(matplot_code)
        exec(matplot_code)


if __name__ == '__main__':
    main()
