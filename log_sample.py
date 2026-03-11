import logging
import employee # when we import a module, it runs the code from that module

# Logging is better than prints. We can control different levels, and pipe to visualization software to get perspective of what is getting logged when
# Logging levels allow us to specify what we want to log by separating into categories. Default level for logging is warning, meaning it will capture everything WARNING and above, ignoring DEBUG and INFO
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.DEBUG is enumed to 10. LEVEL and above get logged
# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# The name is the name of the logger. Since we did not specify a specific logger, we're working with root logger. Not necessarily problematic, but better to get into habit of working with specific loggers that can log separately.
# If we import employee, it runs the code from that module, which includes configuring the root logger. So when we configure the logger again here, it is already configured. The result is employee.log gets created, but NOT test.log, and the employee log config is used, not the one here. Until we set the custom logger in employee.py, then we solved the problem

# Make a custom logger for this file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.ERROR) # Now that we have logging set up like this, we have flexibility. We can set errors or worse to get logged in 1 file, and others to get logged in another file. We can set levels in file handlers themselves
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler) # We set logging level for file_handler. Now stream_handler prints everything to screen. We don't need to set level here if we don't want to

logger.addHandler(file_handler)

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
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception("Tried to divide by 0") # Instead of logging.error, logging.exception includes traceback
    else:
        return result

num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
print(f'Add: {num_1} + {num_2} = {add_result}')
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
print(f'Sub: {num_1} - {num_2} = {sub_result}')
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
print(f'Mul: {num_1} * {num_2} = {mul_result}')
logger.error(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
print(f'Div: {num_1} / {num_2} = {div_result}')
logger.critical(f'Div: {num_1} / {num_2} = {div_result}')