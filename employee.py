import logging
logging.basicConfig(filename="employee.log", level=logging.INFO, format=':%(levelname)s:%(message)s') # So INFO and above get logged

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        logging.info(f"Created Employee: {self.fullname} - {self.email}")

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