import math

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    return b/a

def log(a, b): # base, x
    if b <= 0 or b == 1:
        raise ValueError()
    elif a <= 0:
        raise ValueError()
    return math.log(b, a)

def exp(a, b):
    return a**b
