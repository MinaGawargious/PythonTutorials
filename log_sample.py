import logging

# Logging is better than prints. We can control different levels, and pipe to visualization software to get perspective of what is getting logged when
# Logging levels allow us to specify what we want to log by separating into categories. Default level for logging is warning, meaning it will capture everything WARNING and above, ignoring DEBUG and INFO
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.DEBUG is enumed to 10. LEVEL and above get logged
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 20

add_result = add(num_1, num_2)
print(f'Add: {num_1} + {num_2} = {add_result}')
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
print(f'Sub: {num_1} - {num_2} = {sub_result}')
logging.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
print(f'Mul: {num_1} * {num_2} = {mul_result}')
logging.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
print(f'Div: {num_1} / {num_2} = {div_result}')
logging.debug(f'Div: {num_1} / {num_2} = {div_result}')