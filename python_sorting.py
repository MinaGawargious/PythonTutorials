my_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_list = sorted(my_list) # sorted accepts any iterable while sort method just works on lists. TODO: review iterables and iterators
print(f"Sorted: {sorted_list}")
print(f"Original: {my_list}")
print(f"Sorted in reverse: {sorted(my_list, reverse=True)}")

my_list.sort() # in-place sort
print(f"Original after in-place sort: {my_list}")

my_tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# my_tup.sort() # AttributeError: 'tuple' object has no attribute 'sort'
sorted_tup = sorted(my_tup)
print(sorted_tup, type(sorted_tup)) # sorted takes any iterable and sorts it, but returns a list, not a tuple

my_dict = {"name": "Corey", "job": "Programming", "age": None, "os": "Mac"}
# my_dict.sort() # AttributeError: 'dict' object has no attribute 'sort'
sorted_dict = sorted(my_dict) # sort the keys. Must be of comparable types, so no string and ints for example
print(sorted_dict) # sort the keys

# print(sorted(my_dict.values())) # Can't compare between str and NoneType
print(sorted(my_dict.items())) # sort based on keys

li = [-6, -5, -3, 1, 2, 3]
sorted_li = sorted(li, key=abs) # pass in a function to use before making a comparison. In this case, the absolute value
print(sorted_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self): # Tells Python how we want it printed out to the screen
        return f"({self.name}, {self.age}, ${self.salary})"
    
e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)
        
employees = [e1, e2, e3]
# sorted_employees = sorted(employees)  # TypeError: '<' not supported between instances of 'Employee' and 'Employee'

def e_sort(emp): # alternative to lambda
    return emp.salary

sorted_employees = sorted(employees, key=lambda e: e.age, reverse=True)
print(sorted_employees)

# Alternative:
from operator import attrgetter
sorted_employees2 = sorted(employees, key=attrgetter("age"))
print(sorted_employees2)