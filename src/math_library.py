############################################################################
# @file math_library.py
# @brief Calculator math library for IVS 2025
# @date 27.3.2025
# @author: Filip Figúr <xfigurf00>
#
# Implementation of tests for calculator library
############################################################################

import math
from decimal import Decimal

## @brief Adds two numbers
## @param a First operand
## @param b Second operand
## @return The result of a+b (Sum)
def add(a, b):
    return (a + b)

## @brief Subtraction of two numbers
## @param a First operand (minuend)
## @param b Second operand (subtrahend)
## @return The result of a-b (difference)
def sub(a, b):
    return (a - b)

## @brief Multiplication of two numbers
## @param a First operand (Multiplicand)
## @param b Second operand (Multiplier)
## @return The result of a*b (Product)
def multiply(a, b):
    return (a * b)

## @brief Division of two numbers
## @param a First operand (Dividend)
## @param b Second operand (Divisor)
## @return The result of a/b (Quotient)
def divide(a, b):
    return (a / b)

## @brief Raises the number (a) to the power of an exponent (b)
## @param a Base number
## @param b Exponent
## @return The result of a raised to the power of b (a^b)
def power(a, b):
    return (a ** b)

## @brief Calculates the b-th root of number a (a and b are real numbers)
## @param a Number under root (radicand)
## @param b Degree of the root (Non-zero integer)
## @return The real b-th root of a 
## @throws ValueError if the operation is undefined or would require complex numbers
def n_root(a, b):
    # CASE Not allowed - complex numbers needed
    if (a < 0 and b % 2 == 0): # n_root(-8,2)
        raise ValueError("Cannot compute\n")
    if (a < 0 and b < 0): # n_root(-8,-2)
        raise ValueError("Cannot compute\n")
    # CASE Undefined - mostly a^(1/0)
    if (a != 0 and b == 0): # n_root(2,0)
        raise ValueError("Undefined\n")
    if (a == 0 and b == 0): # n_root(0,0)
        raise ValueError("Undefined\n")
    if (a == 0 and b < 0): # n_root(0,-1)
        raise ValueError("Undefined\n")
    # Valid Input - Compute real root
    if a < 0: # n_root(-27, 3) -> -(-(-27)^(1/3)) = -3 
        root = -((-a) ** (1 / b))
    else:
        root = a ** (1 / b)
    # Round when result is very close to an integer
    if math.isclose(root, round(root), abs_tol=1e-9):
        return round(root)
    return root

## @brief Calculates factorial of positive integer a
## @param a Positive integer and (a < 20)
## @return Factorial of number a
## @throws ValueError if the input is float, negative or greater than 20
def factorial(a):
    if isinstance(a, float): # Basic factorial function is defined only for positive integers
        raise ValueError("Decimal numbers are not allowed")
    if a < 0: 
        raise ValueError("Factorial expects positive integer or zero\n")
    if a > 50: # 50! = very very very VERY big number so it should be enough (65 digits)
        raise ValueError("Overflow\n")
    if a == 0 or a == 1:
        return 1
    result = 1
    counter = 1
    while counter <= a:
        result *= counter
        counter += 1
    return result

## @brief Calculates modulo of a/b
##        In Python, result of modulo (%) has same sign as the divisor
##        Formula for modulo: Dividend mod Divisor = Remainder
##        Proof:  Quotient * Divisor + Remainder = Dividend
## @param a First operand (Dividend)
## @param b Second operand (Divisor)
## @return The result of a%b (Remainder)
def modulo(a, b):
    if b == 0:
        raise ValueError("Division by zero\n")
    if isinstance(a, float) or isinstance(b, float):
        a = Decimal(str(a))
        b = Decimal(str(b))
        result = a % b
        # Result should be positive if b is positive
        if result < 0 and b > 0:
            result += b
        # Result should be negative if b is negative
        elif result > 0 and b < 0:
            result -= b
        return result
    else:
        result = a % b
        return result
