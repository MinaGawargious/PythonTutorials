# Variable scope: LEGB: Local, Enclosing, Global, Built-In

# Local: Variables defined inside a function
# Enclosing: Variables defined inside local scope of enclsoing functions
# Global: Variables defined at top level of a module or explicitly declared gloabl using the global keyword
# Built-In: Variables built in to Python
# This is the order where Python checks variables. First local, then enclosing, then global, then built-in. So one type can mask a variable of the same name from the other type

x = "global x" # global since it's in main body of our file

def test():
    y = "local y"
    print(y)
    print(x) # prints global x. No x in local scope. None in enclosing. But x is in global scope
    
test()
# print(y) # NameError: name 'y' is not defined. y is local to test(). No y in local, enclosing, global, or built-in at this point
print(x) # global x

def test2():
    # global x # Tell Python to use GLOBAL X. This sets the GLOBAL x variable to local x if we uncomment this line. Even if x doesn't yet exist, this line would create the global x
    x = "local x"
    print(x) # local x. Local is checked first before Global
    
test2()
print(x) # global x. x is not re-written by test2() call. 

def test3(z):
    # z is a local variable inside test3
    x = "local x"
    print(z)
    
test3("local z")
# print(z) # NameError: name 'z' is not defined

m = min([5, 1, 4, 2, 3]) # min is a built-in name
print(m)

import builtins
# print(dir(builtins)) # dir gets list of attribute on given object
# def min():
#     print("global min overrides builtin min")
    
# min([5, 1, 4, 2, 3])

# Local still:
def local_test():
    x = "local_test x"
    print(x)
    for i in range(5):
        x = i 
        print(x, i)
    print(x, i) # gets 4, which is the last value local x was set to in for loop. So for loop scope is the same as local scope. We can also access i
    
local_test()
print(x)

def outer():
    x = "outer x"
    print(x)
    
    def inner():
        # x = "inner x"
        print(x) # If line above is commented out, we use inner x. Else, we look to see if there is an x variable in the local scope of any enclosing function. In this case, outer() has x set to "outer x"
	
    inner()
    print(x) # local to inner scope. So we print "outer x". If "outer x" line is commented out, we DO NOT use inner()'s x. We use global x if it exists (LEGB, no local, no enclosing, use global if it exists, else no builtin x so throw error)

print("outer start:")
outer()
print(x)

def outer2():
    x = "outer x 2"
    print(x) # outer x 2
    
    def inner2():
        nonlocal x
        x = "inner x 2" # this is outer2()'s x due to nonlocal statement
        print(x) # inner x 2
	
    inner2()
    print(x) # prints inner x 2
    
outer2()
print(x) # global x