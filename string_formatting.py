person = {"name": "Jenn", "age": 23}

# String concatenation:
sentence = "My name is " + person["name"] + " and I am " + str(person["age"]) + " years old." # String concatenation: open and close quotes everywhere, plus signs everywhere, casting to string is required, remember to put spaces when needed. It's an unreadable mess
print("String concatenation:", sentence)

# C-style % syntax
sentence = "My name is %s and I am %d years old." %(person["name"], person["age"])
print("C Style format:", sentence)

# String format:
sentence = "My name is {} and I am {} years old.".format(person["name"], person["age"]) # Much cleaner and more readable. First value to first placeholder, second value to second placeholder
print("String formatting:", sentence) 

# Number the placeholders in a string format
sentence = "My name is {1} and I am {0} years old.".format(person["name"], person["age"]) # We can explicitly number our placeholders. Here I am mixing age and name on purpose for demonstration purposes. If index out of bounds, we get IndexError: Replacement index 2 out of range for positional args tuple. Here, sentence = My name is 23 and I am Jenn years old.
print("String formatting with placeholders:", sentence)

tag = "h1"
text = "This is a headline"
sentence = "<{0}>{1}</{0}>".format(tag, text)
print(sentence)

# Get a field directly from the placeholder:
sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print("String format getting field directly from placeholder:", sentence)

l = ["Jenn", 23]
sentence = "My name is {0[0]} and I am {0[1]} years old.".format(l)
print("String format getting index directly from placeholder:", sentence)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Jack", 33)
sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)
print("String format getting attribute directly from placeholder:", sentence)

# Keyword arguments to format:
sentence = "My name is {name} and I am {age} years old.".format(name = "Jenn", age = 30)
print("String format with keyword args:", sentence)

sentence = "My name is {name} and I am {age} years old.".format(**person)
print("String format with keyword args and unpacking:", sentence)

# Formatting numbers:
for i in range(1, 11):
    sentence = "The value is {:02}".format(i) # Add formatting to placeholders with colon. :02 zero pads to 2 digits
    print(sentence)
print("Z filled:", "3".zfill(2)) # zfill also worksS
    
pi = 3.14159265
sentence = "Pi is equal to {:.2f}".format(pi) # :.2f means 2 decimal places
print(sentence)

sentence = "1 MB is equal to {:,} bytes".format(1000**2) # :, means format to have commas
print(sentence)

sentence = "1 MB is equal to {:,.2f} bytes".format(1000**2) # :, means format to have commas and .2f means 2 decimal places. We can chain these formats together
print(sentence)

# Formatting dates:
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# What if instead we want March 01, 2016 format
sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

# What if instead we want March 01, 2016 fell on a Tuesday and was the 061 day of the year
sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date) # Can't mix and match between numbered format and non-numbered. So must specify 0 before : for every one, or none of them. Else we get error: ValueError: cannot switch from automatic field numbering to manual field specification
print(sentence)

# f strings for simpler formatting
sentence = f"My name is {person['name']} and I am {person['age']} years old."
print("F string:", sentence)