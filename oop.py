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
        return f"{self.first} {self.last}"
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # self.pay = int(self.pay * raise_amount) # We still need to access class variables through class itself or instance of the class. This raises a NameError: name 'raise_amount' is not defined
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee_new.raise_amount) # same as above, so long as we don't create a raise_amount for a specific instance. Using self allows any subclass to also override it if they wanted to
        
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