import unittest
from employee_to_test import Employee

from unittest.mock import patch # Can use patch as decorator or context manager. Allows us to mock object during test, then object is restored after test is run

class TestEmployee(unittest.TestCase):
    
    # Run before every single test
    def setUp(self):
        # DRY: Don't Repeat Yourself
        print("SetUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000) # instance attributes now
        self.emp_2 = Employee("Sue", "Smith", 60000)
    
    # Run after every single test. We could delete a db here if we created one in each test, for example
    def tearDown(self):
        print("tearDown")
        
    # Run before anything. Useful for populating a database, for example
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    # Run after everything
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch("employee_to_test.requests.get") as mocked_get:
            # The point is to make sure we correctly called the right URL. But if the site is down, we don't want to fail since unittests should test OUR code. So, do the get, but mock the result
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            
            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")
            
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule("June")
            # mocked_get.assert_called_with("http://company.com/Smith/May") # AssertionError: expected call not found. Expected: get('http://company.com/Smith/May') Actual: get('http://company.com/Smith/June')
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")

if __name__ == "__main__":
    unittest.main()
    
# Note: tests don't necessarily run in order. Never assume order. Tests should also be independent.