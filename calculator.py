"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

part 1 - Julia Kowaleski
part 2 - Ronin Mithaug
"""

import math
def add(a, b):
    return a + b
def subtract(a,b):
    return (a-b)
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        return "Division by zero"

def logarithm(a, b):
    try:
        log = math.log(b, a)
        return log
    except ValueError:
        return 'logarithm failed'
def exp(a, b):
    return a ** b
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        if a<0:
            return 'value error'
def hypotenuse(a, b):
    return math.hypot(a, b)




