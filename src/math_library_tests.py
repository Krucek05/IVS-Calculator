############################################################################
# @file math_library_tests.py
# @brief Calculator Tests for IVS 2025
# @date 23.3.2025
# @author: Kristian Rucek <xrucekk00>
#
# Implemenation of tests for calculator library
# Example of testing :  pytest -v math_library_tests.py
#                       python3 -m unittest math_library_tests.py
#                       python3 math_library_tests.py
############################################################################

import unittest
import math
from math_library import add, sub, multiply, divide, power, n_root, factorial, modulo

## 
# @class CalculatorBasicFunctions
# @brief A calculator class that performs basic arithmetic operations.
##
class CalculatorBasicFunctions(unittest.TestCase) :
  
  ## @brief Test the add function with equivalence classes.
  def test_add(self):
    self.assertEqual(add(1, 2), 3)
    self.assertEqual(add(1000, 157), 1157)
    self.assertEqual(add(110545545, 4454515), 115000060)
    self.assertEqual(add(2147483647, 1), 2147483648)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(0, 0), 0)
    self.assertEqual(add(1, -1), 0)
    self.assertEqual(add(-1, -1), -2)
    self.assertEqual(add(-1000, -145), -1145)
    self.assertEqual(add(-2147483648, -1), -2147483649)
    self.assertTrue(math.isclose(add(0.12345, 0.9876), 1.11105, rel_tol=1e-9))  #used to check precision
    self.assertTrue(math.isclose(add(1.0000001, 2.0000002), 3.0000003, rel_tol=1e-9))
    self.assertTrue(math.isclose(add(-0.54321, 0.54321), 0.0, rel_tol=1e-9))
  
  ## @brief Test the sub function with equivalence classes.
  def test_sub(self):
    self.assertEqual(sub(1, 2), -1)
    self.assertEqual(sub(1000, 157), 843)
    self.assertEqual(sub(110545545, 4454515), 106091030)
    self.assertEqual(sub(2147483647, 1), 2147483646)
    self.assertEqual(sub(-1, 1), -2)
    self.assertEqual(sub(0, 0), 0)
    self.assertEqual(sub(1, -1), 2)
    self.assertEqual(sub(-1, -1), 0)
    self.assertEqual(sub(-1000, -145), -855) 
    self.assertEqual(sub(-2147483648, -1), -2147483647)
    self.assertTrue(math.isclose(sub(0.9876, 0.12345), 0.86415, rel_tol=1e-9))
    self.assertTrue(math.isclose(sub(5.5, 2.2), 3.3, rel_tol=1e-9))
    self.assertTrue(math.isclose(sub(-10.1, -5.05), -5.05, rel_tol=1e-9))

  ## @brief Test the multiply function with equivalence classes.
  def test_multiply(self):
    self.assertEqual(multiply(1, 2), 2)
    self.assertEqual(multiply(1000, 157), 157000)
    self.assertEqual(multiply(110545545, 4454515), 492439722629717)
    self.assertEqual(multiply(2147483647, 1), 2147483647)
    self.assertEqual(multiply(-1, 1), -1)
    self.assertEqual(multiply(0, 0), 0)
    self.assertEqual(multiply(1, -1), -1)
    self.assertEqual(multiply(-1, -1), 1)
    self.assertEqual(multiply(-1000, -145), 145000)
    self.assertEqual(multiply(-2147483648, -1), 2147483648)
    self.assertTrue(math.isclose(multiply(0.1234, 0.9876), 0.12189984, rel_tol=1e-9))
    self.assertTrue(math.isclose(multiply(3.14159, 2.0), 6.28318, rel_tol=1e-9))
    self.assertTrue(math.isclose(multiply(-2.5, 4.0), -10.0, rel_tol=1e-9))

  ## @brief Test the divide function with equivalence classes.
  def test_divide(self):
    self.assertEqual(divide(1, 2), 0.5)# to check precision
    self.assertEqual(divide(110545545, 4454515), 24.8)
    self.assertEqual(divide(2147483647, 1), 2147483647)
    self.assertEqual(divide(-1, 1), -1)
    self.assertEqual(divide(0, 1), 0)
    self.assertEqual(divide(1, -1), -1)
    self.assertEqual(divide(-1, -1), 1)
    self.assertEqual(divide(-2147483648, -1), 2147483648)
    self.assertTrue(math.isclose(divide(0.9876, 0.1234), 8.00486, rel_tol=1e-5))
    self.assertTrue(math.isclose(divide(5.5, 2.2), 2.5, rel_tol=1e-9))
    self.assertTrue(math.isclose(divide(-10.1, -5.05), 2.0, rel_tol=1e-9))
    
  def test_divide_by_zero(self):
      with self.assertRaises(ZeroDivisionError):
         divide(10, 0)  # This should raise ZeroDivisionError

##
# @class CalculatorAdvancedFunctions
# @brief A calculator class that performs advanced arithmetic operations.
##
class CalculatorAdvancedFunctions(unittest.TestCase) :

  ## @brief Test the exponent function with equivalence classes.
  def test_power(self):
    self.assertEqual(power(2, 3), 8)
    self.assertEqual(power(5, 0), 1)
    self.assertEqual(power(0, 5), 0)
    self.assertEqual(power(0, 0), 1)
    self.assertEqual(power(-2, 3), -8)
    self.assertEqual(power(2, -3), 0.125)
    self.assertTrue(math.isclose(power(2, 0.5), 1.414213562, rel_tol=1e-9))  # Square root of 2
    self.assertEqual(power(10, 2), 100)
    self.assertEqual(power(-3, 2), 9)  


  ## @brief Test the square_root function with equivalence classes.
  def test_n_root(self):
    self.assertTrue(math.isclose(n_root(4, 2), 2, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(27, 3), 3, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(81, 4), 3, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(16, 2), 4, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(1000, 3), 10, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(100, 2), 10, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(1024, 10), 2, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(256, 8), 2, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(1, 3), 1, rel_tol=1e-9))
    self.assertTrue(math.isclose(n_root(625, 4), 5, rel_tol=1e-9))
    self.assertRaises(ValueError, n_root, -16, 0.5)  # should raise error (floats are not allowed)
    self.assertRaises(ValueError, n_root, -1, 3)  #should raise error (negatives are not allowed)
    self.assertRaises(ValueError, n_root, 0, 0)  # should raise error
    self.assertRaises(ValueError, n_root, -1, -1)  # should raise error (negatives are not allowed)
    self.assertRaises(ValueError, n_root, 1, 0)  # should raise error
    self.assertRaises(ValueError, n_root, 0, -3)  # should raise error (negatives are not allowed)
    
  ## @brief Test the factorial function with equivalence classes.
  def test_factorial(self):
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(10), 3628800)
    self.assertEqual(factorial(20), 2432902008176640000)
    self.assertRaises(ValueError, factorial, 21) # should raise error, too big
    self.assertRaises(ValueError, factorial, -1)  # should raise error (negatives are not allowed)
    self.assertRaises(ValueError, factorial, -10) # should raise error (negatives are not allowed)
    self.assertRaises(ValueError, factorial, 2.5) # should raise error (floats are not allowed)
    
  ## @brief Test the modulo function with equivalence classes.
  def test_modulo(self):
    self.assertEqual(modulo(0,1), 0)
    #self.assertEqual(modulo(5.2), 1)
    self.assertEqual(modulo(5,5), 0)
    self.assertEqual(modulo(10,1), 0)
    self.assertEqual(modulo(2000,7), 5)
    #self.assertEqual(modulo(-1, 2), -1) 
    #self.assertEqual(modulo(2, -3), 2)
    self.assertEqual(modulo(-40, -6), -4) 
    self.assertEqual(modulo(999, 1000), 999)
    self.assertEqual(modulo(1000, 999), 1)
    self.assertEqual(modulo(10**10, 3), 1)
    self.assertTrue(math.isclose(modulo(5.5, 2.2), 1.1, rel_tol=1e-9))
    self.assertTrue(math.isclose(modulo(-7.5, 3.2), 2.1, rel_tol=1e-9))
    self.assertTrue(math.isclose(modulo(0.3, 0.1), 0.0, rel_tol=1e-9))
    self.assertRaises(ValueError, modulo, 5645, 0)  # Should raise an error (division by zero)

  if __name__ == "__main__":
    unittest.main()