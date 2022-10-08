from fractions import Fraction

def get_value():
    return Fraction(input('Insert a fraction: '))

def get_operator():
    return input('Insert an operator: ')

def get_result(res):
    print(f'The result: {Fraction(res)}')
