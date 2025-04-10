"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
a = 10
b = 1
import math
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