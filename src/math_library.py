############################################################################
# @file math_library.py
# @brief Calculator math library for IVS 2025
# @date 27.3.2022
# @author: Filip Figúr <xfigurf00>
#
# Implemenation of tests for calculator library
############################################################################

import math
from decimal import Decimal
"""
@brief ADD function
"""
def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

def power(a,b):
    return (a**b)

def n_root(a,b):
    #if ((isinstance(a,float)) or (isinstance(b,float))):
    #    raise ValueError("Floats are not allowed\n")
    if ((a < 0) and (b % 2 == 0)):#n_root(-8,2)
        raise ValueError("Cannot compute\n")
    if ((a < 0) and (b < 0)):
        raise ValueError("Cannot compute\n")
    if (((a != 0) and (b == 0)) or ((a == 0) and (b == 0)) or ((a == 0) and (b < 0))): #n_root(2,0) or #n_root(0,0)
        raise ValueError("Undefined\n")
    if ((a == 0) and (b == 0)):
        raise ValueError("Undefined\n")
    
    if a < 0:
        root = -((-a) ** (1 / b))
    else:
        root = a ** (1 / b)
    if math.isclose(root, round(root), abs_tol=1e-9):
        return round(root)
    return root

"""
Limit for factorial should be enough
"""
def factorial(a):
    if (isinstance(a,float)):
        raise ValueError("Floats are not allowed")
    if (a < 0):
        raise ValueError("Factorial expects natural number or zero\n")
    if (a > 20):
        raise ValueError("Overflow\n")
    if ((a == 0) or (a == 1)):
        return 1
    result = 1
    counter = 1
    while (counter <= a):
        result *= counter
        counter += 1
    return(result)

"""
Formula for modulo: Dividend mod Divisor = Remainder
Proof:  Quotient * Divisor + Remainder = Dividend
"""
def modulo(a,b):
    if (b == 0):
        raise ValueError("Division by zero\n")
    if ((isinstance(a,float)) or (isinstance(b,float))):
        a = Decimal(str(a))
        b = Decimal(str(b))
        result = a % b
        # result should be positive if b is positive
        if ((result < 0) and (b > 0)):
            result += b
        # result should be negative if b is negative
        elif ((result > 0) and (b < 0)):
            result -= b
        return (result) 
    else:
        result = a % b
        return (result)