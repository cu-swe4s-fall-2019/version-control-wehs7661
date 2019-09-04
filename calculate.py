import math_lib
import argparse

def initialize():
    parser = argparse.ArgumentParser(
        description = 'This code calculate a + b + (a/b) given the values of a and b' 
    )
    parser.add_argument('-a',
                        '--value_a',
                        help='The value of a'
    )
    parser.add_argument('-b',
                        '--value_b',
                        help='The value of b'
    )

    args_parse = parser.parse_args()

    return args_parse

if __name__ == "__main__":
    args = initialize()
    a = float(args.value_a)
    b = float(args.value_b)
    result = math_lib.add(a, b) + math_lib.div(a, b) 
    print('The value of a: ', a)
    print('The value of b: ', b)
    print('The value of a + b + (a/b): ', result)