# First class functions allow us to treat functions like any other object. We can pass functions as arguments to another function, we can return functions, and we can assign functions to variables
# Closures allow us to take advantage of first-class functions and return an inner function that remembers and has access to variables local to the scope in which they were created

# Hella confusing. Need review before using tbh
# TODO: Review this. Like, a lot. Like, a lot a lot

def outer_function():
    message = "Hi"
    
    def inner_function():
        print(message)
        # message wasn't created in inner_function(), but inner_function() has access to it. This is what is called a free
    
    return inner_function()

x = outer_function()
print(f"x = {x}")

def outer_function2():
    message = "Hi"
    
    def inner_function():
        print(message)
    
    return inner_function # Return inner_function without executing

my_func = outer_function2()
print(f"my_func = {my_func}")
print(f"my_func() = {my_func()}") # Returns none, prints "Hi"
my_func()
my_func() # Prints message variable Hi multiple times. That's what a closure is: it remembers our message variable even when our outer_function has finished executing

# TODO: deep dive into first-class functions and closures

def outer_function3(msg):
    message = msg
    
    def inner_function():
        print(message)
    
    return inner_function

hi_func = outer_function3("Hi")
bye_func = outer_function3("Bye")

hi_func()
bye_func()

def outer_function4(msg):
    def inner_function():
        print(msg)
    
    return inner_function

hi_func = outer_function4("Hi Again")
bye_func = outer_function4("Bye Again")

hi_func()
bye_func()

# Decorators: a function that takes another function as an argument, adds functionality, and returns another function, without altering source code of original function passed in:
def decorator_function(original_function):
    def wrapper_function():
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function() # Take in original_function, alter it or do stuff before, then run it

    return wrapper_function # then return a new function waiting to be executed. When it is executed, it runs wrapper_function() with its 0 or more alterations on original_function

def display():
    print("display function ran")
    
decorated_display = decorator_function(display)
decorated_display()

# Another way to do decorator functions. Identical to above (display2 = decorator_function(display2); display2())
@decorator_function
def display2():
    print("display2 function ran")
    
display2()

def display_info(name, age):
    print(f"display_info ran with arguments {name} {age}")
    
display_info("Mina", 27)

# TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 1 was given:
# @decorated_display
# def display_info2(name, age):
#     print(f"display_info ran with arguments {name} {age}")
    
# display_info2("Mina", 25)

# To pass in args to decorated function, use *args and **kwargs:
def decorator_function2(original_function):
    def wrapper_function(*args, **kwargs): # *args and **kwargs allow us to accept any number of args and keyword args to our function
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function

@decorator_function2
def display_info2(name, age):
    print(f"display_info ran with arguments {name} {age}")

display_info2("Mina", 25)

# We can also have decorator classes vs. decorator functions
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function # tie function to instance of class
        
    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        self.original_function(*args, **kwargs)
        
@decorator_class
def display_info3(name, age):
    print(f"display_info ran with arguments {name} {age}")

display_info3("Mina", 25)

# Why not have another function that does what it needs to do, then calls the original function we pass in:
def do_stuff2(do_stuff):
    print("did stuff 2")
    do_stuff()

def test():
    print("testing")
    
do_stuff2(test)

def decorator_func(original_func, *args, **kwargs):
    print("ran decorator")
    original_func(*args, **kwargs)

def print_msg(msg, name="Mike"):
    print(f"testing {msg} {name}")
    
decorator_func(print_msg, "hi", name = "Mina")

# Practical example
from functools import wraps # prevents the wrapper function's name from being returned, overriding orig_func name

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO) # Set up log file matching name of original function

    @wraps(orig_func)
    def wrapper(*args, **kwargs): # create wrapper and take in args and kwargs
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        print(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs) # Run orig_func before leaving wrapper

    return wrapper # return wrapper that lets us run all this with the added functionality

# Decorator allows us to add functionality in 1 location and exaseasily apply it with 1 line
@my_logger
def display_info_logger(name, age):
    print(f"display_info_logger ran with arguments {name} {age}")
    
display_info_logger("Michael", 29)

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper

@my_timer
def display_info_logger2(name, age):
    print(f"display_info_logger2 ran with arguments {name} {age}")
    
result = display_info_logger2("Michael", 29)
print(result) # returned from wrapper. None in this case since display_info_logger returns None

# We can also stack decorators:
print("\n\n")

@my_timer
@my_logger
def display_info_logger3(name, age):
    print(f"display_info_logger3 ran with arguments {name} {age}")
    
# equal to display_info_logger3 = my_logger(my_timer(display_info_logger3))
# But names can get screwed up:
display_info_logger3 = my_timer(display_info_logger3)
print(display_info_logger3.__name__) # wrapper. Fixed with @wraps decorator
    
display_info_logger3("Michael", 29)
# TODO: Why did I not get wrapper.log when testing without the @wraps() decorator? Did behavior change between 2016 and now?