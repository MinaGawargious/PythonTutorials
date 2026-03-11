# Python Object-Oriented Programming

# Classes in all languages allow us to logically group data (attributes) and functions (methods) in a way that's easy to reuse and built upon

# Each employee has a name, email address, pay, and actions they can perform, so this lends itself nicely to a class
class Employee:
    pass

# Class is a blueprint for creating instances. Instance variables contain data unique to each instance
emp1 = Employee() # instance of Employee class
emp2 = Employee() # instance of Employee class
print(emp1, emp2)

# instance variables only for emp1, not emp2 or Employee class as a whole
emp1.first = "Mina"
emp1.last = "Gawargious"
emp1.email = "Mina.Gawargious@company.com"
emp1.pay = 100000
print(dir(Employee))
print(dir(emp1)) # has first, last, and email
print(dir(emp2)) # same as Employee
print(emp1.pay)
# print(emp2.pay) # AttributeError: 'Employee' object has no attribute 'pay'

# The above is annoying to manually set for each employee, and is error prone if we make a typo or forget an attribute. Instead, have a constructor or initializer:

class Employee_new:
    raise_amount = 1.04
    num_employees = 0
    def __init__(self, first, last, pay): #Constructor/initializer. All methods within a class receive the instance as the first argument automatically. By convention called self. TODO: why explicit self needed?
        self.first = first # Same as above emp1.first = "Mina", but now we do it in constructor for each employee
        self.last = last # don't need to be same name. Could be self.lname = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        
        Employee_new.num_employees += 1 # Makes no sense to use self here. This is a general class variable
        
    def fullname_error():
        return f"{self.first} {self.last}" # Must pass in self
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # self.pay = int(self.pay * raise_amount) # We still need to access class variables through class itself or instance of the class. This raises a NameError: name 'raise_amount' is not defined
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee_new.raise_amount) # same as above, so long as we don't create a raise_amount for a specific instance. Using self allows any subclass to also override it if they wanted to
        
    # Normal methods take in self. Class methods do not. Indicate classmethods with decorator
    @classmethod # Receive CLASS as first argument, not self
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str): # alternative consructor
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    # regular instance methods take in instance self implicitly, class methods take in class cls implcitly, and static methods don't take in anything automatically. They're just like normal functions, but we include them in our class because they have some logical connection to our clas
    
    # has logical connection to our class, but doesn't depend on any instance or class variable. If we don't access instance or class within method, that's a giveaway that it's a static method
    @staticmethod
    def isworkday(day):
        return not (day.weekday() == 5 or day.weekday() == 6) # 5 or 6 is Sat or Sun, so if that's true, return false
        
emp1 = Employee_new("Mina", "Gawargious", 100000) # When creating new Employee_new object, we can leave off self since it's passed automatically
emp2 = Employee_new("Test", "User", 50000) 
print(emp1)
print(emp1.email)
print(f"Full name = {emp1.first} {emp1.last}")
print(f"emp1.fullname() =", emp1.fullname()) 
# emp1.fullname() pass in emp1 instance implictly, but it is the same as running at the class level and passing in instance explictly
print(f"Employee_new.fullname(emp1) =", Employee_new.fullname(emp1)) # emp1.fullname() gets transformed into Employee_new.fullname(emp1) in the background, hence the explicit self
# print(f"emp1.fullname_error() =", emp1.fullname_error()) # TypeError: Employee_new.fullname_error() takes 0 positional arguments but 1 was given. This means self is automatically passed as an arg

# instance variables are unique for each instance, and use self. Class variables are shared among all instances of a class. They are the same for each instance
print(emp1.pay, emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.pay, emp2.pay) # The 1.04 can be a class variable if it's the same across instances. Right now, we have no way to access it or change it easily if it's in multiple places in our code. Unless we pull it into a class variable raise_amount

# When we try to access an attribute on an instance, we first check instance for  attribute. If it doesn't exist, it sees if the class or any class it inherits from has it. So if we do emp1.__dict__, raise_amount WON'T show up, but Employee_new.__dict__ DOES have it
print("emp1.__dict__ =", emp1.__dict__) # no raise_amount
print("Employee_new.__dict__ =", Employee_new.__dict__)

# So if we do Employee.raise_amount, it changes it for all variables
Employee_new.raise_amount = 1.05
print(emp1.raise_amount) # 1.05
print(emp2.raise_amount) # 1.05
print(Employee_new.raise_amount) # 1.05

# But if I change emp1.raise_amount = 1.06, it CREATES raise_amount as a instance variable in emp1's own namespace. Then emp1's instance checks THAT raise_amount first and not the Employee_new.raise_amount which stays at 1.05
emp1.raise_amount = 1.06
print("emp1.raise_amount =", emp1.raise_amount) # 1.06
print("emp2.raise_amount =", emp2.raise_amount) # 1.05
print("Employee_new.raise_amount =", Employee_new.raise_amount) # 1.05

print("emp1.__dict__ =", emp1.__dict__) # raise_amount: 1.06
print("emp2.__dict__ =", emp2.__dict__) # no raise_amount. use class's
print("Employee_new.__dict__ =", Employee_new.__dict__) # raise_amount = 1.05

print(Employee_new.num_employees) # 2

emp1.set_raise_amount(1.1) # Automatically passes in class implcitly. Frowned upon
print("emp1.raise_amount =", emp1.raise_amount) # 1.06 (from its own namespace)
print("emp2.raise_amount =", emp2.raise_amount) # 1.1 (from Employee_new class)
print("Employee_new.raise_amount =", Employee_new.raise_amount) # 1.1

Employee_new.set_raise_amount(1.2) # Automatically passes in class implcitly
print("emp1.raise_amount =", emp1.raise_amount) # 1.06 (from its own namespace)
print("emp2.raise_amount =", emp2.raise_amount) # 1.2 (from Employee_new class)
print("Employee_new.raise_amount =", Employee_new.raise_amount) # 1.2

# We can also use class methods as alternative constructors. Say we have employee data in the form of strings and we want to build instances based off that
emp_str = "John-Doe-70000"
# Instead of splitting based on - and creating a new employee, we can pass in string DIRECTLY with an alternative constructor

emp3 = Employee_new.from_string(emp_str)
print(emp3)
print(Employee_new.num_employees)

import datetime
my_date = datetime.date(2016, 7, 10)
print(f"Employee_new.isworkday(my_date) =", Employee_new.isworkday(my_date))

# Class inheritance allows us to inherit attributes and methods of a parent class and allow us to create subclasses with the functionality of a parent class
# Developer and manager subclasses will have names, emails, and pay, so we can inherit from Employee_new class
class Developer(Employee_new): # Inherit from Employee_new class
    raise_amount = 1.5 # In the method resolution order, we would encounter 1.5 first
    
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay) # Let superclass handle first, last, and pay
        # Employee_new.__init__(self, first, last, pay) # Same as above for single inheritance, but super() is still cleaner
        self.programming_language = programming_language

dev_1 = Developer("Mina", "Gawargious", 100000, "Python") # Python looked at Developer class for constructor, did not find it, then walked up chain of inheritance until if found what it's looking for. Chain is called method resolution order, which is order where Python looks for attributes and methods
dev_2 = Developer("Test", "Employee", 60000, "Java")

print(isinstance(dev_1, Employee_new), isinstance(dev_1, Developer)) # True True
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.programming_language)

# print(help(Developer)) # Very useful

class Manager(Employee_new):
    def __init__(self,  first, last, pay, employees=None): # We don't pass in [] as default arg because we don't want to pass in a mutable argument like list or dict as a default arg
        super().__init__(first, last, pay)
        self.employees = employees if employees else []
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_employees(self):
        for employee in self.employees:
            print("-->", employee.fullname())
            
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_employees()
mgr_1.add_emp(dev_2)
mgr_1.print_employees()
mgr_1.remove_emp(dev_1)
mgr_1.print_employees()

# isinstance will tell us if an object is an instance of a class
print("isinstance(mgr_1, Manager) =", isinstance(mgr_1, Manager)) # True
print("isinstance(mgr_1, Developer) =", isinstance(mgr_1, Developer)) # False
print("isinstance(mgr_1, Employee_new) =", isinstance(mgr_1, Employee_new)) # True

# issubclass will tell us if an object is an instance of a class
print("issubclass(Manager, Manager) =", issubclass(Manager, Manager)) # True
print("issubclass(Manager, Developer) =", issubclass(Manager, Developer)) # False
print("issubclass(Manager, Employee_new) =", issubclass(Manager, Employee_new)) # True
print("issubclass(Employee_new, Manager) =", issubclass(Employee_new, Manager)) # False