"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def add(a, b): 
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return (b/a)
except ZeroDivisionError as e: #zerodivisionerror is already in python
    print(str(e))
except:
    print("Something went wrong")


