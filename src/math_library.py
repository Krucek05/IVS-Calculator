############################################################################
# @file math_library.py
# @brief Calculator math library for IVS 2025
# @date 27.3.2022
# @author: Filip Figúr <xfigurf00>
#
# Implemenation of tests for calculator library
############################################################################

import math
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
    return(a**(1/b))
"""
Limit for factorial should be enough
"""
def factorial(a):
    if isinstance(a,float):
        raise ValueError("Floats are not allowed")
    if a < 0:
        raise ValueError("Factorial expects natural number or zero\n")
    if a > 20:
        raise ValueError("Overflow\n")
    if a == 0 or a == 1:
        return 1
    result = 1
    counter = 1
    while (counter <= (a)):
        result *= counter
        counter += 1
    return(result) 
"""
Formula for modulo: Dividend mod Divisor = Remainder
Proof:  Quotient * Divisor + Remainder = Dividend
"""
def modulo(a,b):
    return (a%b)  






    
 