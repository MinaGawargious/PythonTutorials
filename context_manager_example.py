# Context managers allow us to properly manage resources so we can specify what to set up and tear down when working with specific objects

f = open("demo2.txt", "w")
f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
f.close()

with open("demo2.txt", "w") as f: # context manager (indicated by with statement). No longer have to close file, and any errors that occur still lead to file being closed
    # This is useful for closing databases automatically, acquiring and releasing locks, etc
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    
# Custom context managers, either through class or function with a decorator

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # Setup of context manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file # object we are working with in our context manager

    # Teardown of context manager
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        
# with statement runs code within the __enter__ method
with Open_File("demo3.txt", "w") as f: # f is what was returned in our __enter__ method
    f.write("Testing123")
    
print(f.closed) # Should return True outside our context manager after we're done

# we can also create our own context managers with a function, using contextlib module and contextmanager decorator
from contextlib import contextmanager # We can use contextmanager decorator to decorate a generator function

# Equivalent to our class above
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)  # everything before yield statement is equivalent to __enter__ method
        yield f # yield is where code within with statement will run. It's like when we return self.file from __enter__ method
        print("A")
    finally:
        f.close() # everything after yield statement is equal to our __exit__ method
        print("exiting")
    
with open_file("demo4.txt", "w") as f2:
    print("B")
    f2.write("Testing123")
    print("done")
    
# TODO: Does yield pause execution? Like will prints inside with statement print before the rest of this code executes? Also just review yield in general
# print order is B done A exiting, so yield is like a pause
    
print(f2.closed)


#### CD Example ####
import os

# Saving cwd and chdir'ing is like __enter__, and printing directory and coming back is like __exit__
cwd = os.getcwd()
os.chdir('My_Module_Dir')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Environments')
print(os.listdir())
os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
        
with change_dir("My_Module_Dir"): # we didn't yield anything in change_dir, so no as f or anything
    os.listdir()

with change_dir("Environments"):
    os.listdir()
    
# Now we don't have to worry about setup and teardown of saving cwd, changing directory, and changing back. Now it's automatically managed by our context manager