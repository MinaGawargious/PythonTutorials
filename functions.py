# Functions take input and execute bundled code and can return a result

def hello_func():
    print("Hello Function")
    
print(hello_func) # <function hello_func at 0x74854df63d90>
print(hello_func()) # Hello Function from function gets printed, then None for the return type of the function

def pass_test():
    pass # Functionc can't be empty, so pass is basically a no-op

pass_test()

def hello_func2():
    return "Hello Function 2"

print(hello_func2())
print(hello_func2().upper()) # Treat return value like the data type that it is, in this case a string, and do normal string operations on it

def hello_func3(greeting):
    return f"Hello {greeting}"

print(hello_func3("Mina"))

# def hello_func4(name="You", greeting): # SyntaxError: non-default argument follows default argument
#     return f"{greeting}, {name}"

def hello_func4(greeting, name="You"): # Default argument of "You" for name. Default arguments must be after non-default arguments (see example above to see why. If we call hello_func4("Hello"), should "Hello" go to greeting and use "You" for name, or should "Hello" go to name and greeting is empty. It is not clear, so default args are after all non-default ones
    return f"{greeting}, {name}"

print(hello_func4("Howdy"))
print(hello_func4(greeting="Ayo", name="Yo"))

# args and kwargs

def student_info(*args, **kwargs):
    print(args) # positional and keyword arguments. We don't know how many there will be, so *args and **kwargs are useful
    print(kwargs)
    
# Positional and keyword are by function CALL. Required and optional are by function DEFINITION. Required argument -> no default value in the DEFINITION. Optional argument -> default value in DEFINITION. Positional -> in function CALL, use position. Keyword -> in function CALL name the parameter you're passing in

student_info("Math", "Art", name="Mina", age = 27) # args are tuple of ('Math', 'Art'). kwargs are dictionary of {'name': 'Mina', 'age': 27}

courses = ["Math", "Art"]
info = {"name": "Mina", "age": 27}

student_info(*courses, **info) # Unpack list and info (if we just do *info, that is a arg (not kwarg) of "name" and "age"). This is equivalent to previous call

# TODO: review positional and keyword arguments in function CALLS, default and non-default parameters in function DEFINITIONS, and *args and **kwargs, and unpacking