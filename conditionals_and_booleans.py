if True:
    print("Conditional was True")
if False:
    print("Conditional was False")
    
language = "Python"
if language == "Python":
    print("Language is Python")
elif language == "Java": # Not Python, yes Java
    print("Language is Java")
elif language == "C": # Not Python or Java, yes C
    print("Language is C")
else: # Not Python, Java, or C
	print("No match")
    
if language is "Python":
    print("Language is Python") # Still prints, but might be implementation-specific with CPython. Use == for equality, and is for identity
    
# Operators: AND, OR, NOT
user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin is logged in")
else: # Either user is not admin, or not logged in (or both since that's how or works)
    print("Invalid credentials")
    
if not logged_in:
    print("Please log in")
else:
	print("Logged in")
 
a = [1, 2, 3]
b = [1, 2, 3]

print(a==b)
print(a is b)
print(id(a), id(b)) # Different objects in memory

b = a
print(a==b)
print(a is b)
print(id(a), id(b)) # Same  objects in memory. Same pointer

b = a[:]
print(a==b)
print(a is b)
print(id(a), id(b)) # Different objects again

# a is be is the same as id(a) == id(b)

# False includes False, None, Zero, empty sequence like '', "", ()/tuple(), []/list(), set(), or empty map/dict {}/dict(). Everything else is True

a = set()
if a:
    print(f"{a} evaluated to True")
else:
    print(f"{a} evaluated to False")