"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
a = 10
b = 1
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero"
def log(a, b):
    try:
        math.log(b, a)
    except:
        return "Log error"
def exp(a, b):
    return a ** b