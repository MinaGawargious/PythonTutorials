# import my_module as mm # In same directory, so okay
from My_Module_Dir.my_module import find_index as fi, test # Now we don't need to preface functionc call with my_module. or mm. We can do fi
# from my_module import * # frowned upon since we can't tell what came from which module

import sys
# sys.append(PATH_TO_DIRECTORY) # If my_module was in a different directory, we could just add to sys.path for this run

courses = ["History", "Math", "Physics", "CompSci"]
index = fi(courses, "History")
print(index)

print(test)

print(sys.path) # This is the list of locations Python looks when it searches for modules. It looks through sys.path in the order in which it appears. We can import from same directory, PYTHONPATH env variable, standard library directories, or site packages directory for 3rd party packages

# sys.path.append("Test123") # Only for this run
# print(sys.path) 

# Better to change the next spot Python looks for modules after the current directory, which is the PYTHONPATH environment variable. Edit .bashrc for Unix terminals, and Windows Environment Variables for CMD
# TODO: .bashrc vs .bash_profile

import random, math, datetime, calendar, os # from standard library
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads) # pi/2
print(math.sin(rads))

print(datetime.date.today())
print(calendar.isleap(2024))

print(os.getcwd()) # cwd = current working directory
print(os.__file__) # prints location of os.py in our system