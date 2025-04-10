"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        if a<0:
            return 'value error'
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return (b/a)
def divide(a,b):
    try:
        return b/a
    except ZeroDivisionError:
        return 'division by zero'
def logarithm(a,b):
    try:
        log = math.log(b,a)
        return log
    except ValueError:
        return 'logarithm failed'
def exponent(a,b):
    return a**b

print(square_root(a))