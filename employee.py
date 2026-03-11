import logging

# Make a custom logger for this file
logger = logging.getLogger(__name__) # When we run module directly, __name__ == __main__, and when we run it from another module, __name__ is equal to module name (employee). If we don't set config, it defaults to root config
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Default logging config
# logging.basicConfig(filename="employee.log", level=logging.INFO, format=':%(levelname)s:%(name)s:%(message)s') # So INFO and above get logged

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

emp1_test = Employee("John", "Smith", 100000)
emp2_test = Employee("Corey", "Schafer", 80000)