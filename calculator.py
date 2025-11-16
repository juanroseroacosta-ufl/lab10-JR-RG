# https://github.com/juanroseroacosta-ufl/lab10-JR-RG
# Partner 1: Juan Rosero Acosta
# Partner 2: Rohan Grewal

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as error:
        raise ValueError()

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    return b / a

def logarithm(a, b): # base, x
    if b <= 0 or b == 1:
        raise ValueError()
    elif a <= 0:
        raise ValueError()
    return math.log(b, a)

def exp(a, b):
    return a ** b