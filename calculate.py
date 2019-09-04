import math_lib
import argparse

def initialize():
    parser = argparse.ArgumentParser(
        description = 'This code calculate a + b + (a/b) given the values of a and b' 
    )
    parser.add_argument('-a',
                        '--value_a',
                        type=float,
                        help='The value of a',
                        required=True
    )
    parser.add_argument('-b',
                        '--value_b',
                        type=float,
                        help='The value of b',
                        required=True
    )

    args_parse = parser.parse_args()

    return args_parse

if __name__ == "__main__":
    args = initialize()
    try: 
        a = float(args.value_a)   # no need to do int(args.valu_a)
    except:
        print('The data type of a should be float or int.')

    try:
        b = float(args.value_b)  # no need to do int(args.valu_b)
    except:
        print('The data type of b should be float or int.')
    
    result = math_lib.add(a, b) + math_lib.div(a, b) 
    print('The value of a: ', a)
    print('The value of b: ', b)
    print('The value of a + b + (a/b): ', result)