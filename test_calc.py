# Testing gives you confidence that any changes don't break your code. Naming convention is to call it test_THINGWERETESTING. In unit tests itself, that's required

import unittest
import calc

class TestCalc(unittest.TestCase): # Inheriting from unittest.TestCase will give us access to the testing capabilities of that class
    # def add_test(self): # MUST start with test_. This won't work
    # def test_something(self): # MUST start with test_. This works since it started with test_. No need to have add after, but nicer and cleaner
    def test_add(self): # MUST start with test_
        # All these assertions are 1 test.
        self.assertEqual(calc.add(10, 5), 15) # Visit https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug to see all options
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        # self.assertEqual(calc.add(10, 5), 14) # All these assertions are 1 test.
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        # first 3 tests pass if we do normal or floor division. So, once we se 5/2 yields 2 instead of 2.5, we can add that case to our tests so we never face it again in the future. Always add to tests as you go
        self.assertEqual(calc.divide(5, 2), 2.5)
        
        # To test exceptions, do this:
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # self.assertRaises(ValueError, calc.divide, 10, 2) # Not an error, so we get: AssertionError: ValueError not raised by divide
        
        # To call the function normally vs. passing in arguments separately, do this with context manager
        with self.assertRaises(ValueError):
            # calc.divide(10, 1) # AssertionError: ValueError not raised
            calc.divide(10, 0)
        
# TODO: review this unittest.main() call. Without these 2 lines, we need to do python3 -m unittest test_calc.py. Why? And what does the -m mean?
if __name__ == "__main__":
    unittest.main()