# Decorators with args

def prefix_decorator(prefix): # everything nested below has access to prefix arg. All we did was add 1 more layer to our decorator functions
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function

# @decorator_function
@prefix_decorator("TESTING:")
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('John', 25)
display_info('Travis', 30)