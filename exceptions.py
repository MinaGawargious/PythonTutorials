try:
    # var = bad_var # NameError: name 'bad_var' is not defined
    f = open("demo.txt") # intentionally open non-existant demo vs. demo.txt
except FileNotFoundError as e: # Exception is generic. We can catch specific exceptions like FileNotFoundError
    print(f"Sorry, this file does not exist: {e}")
except Exception as e:
    print(f"Sorry, something went wrong: {e}")
else: # if the try clause did NOT raise an exception. We could move this to the try section, but it may raise an exception we didn't intend, so okay to keep it here
    # TODO: when would I legit use try else
    print("Executing else")
    print(f.read())
    f.close()
finally: # Runs always. Regardless of success or failure. Helpful to release resources, for example
    print("Executing finally\n")
    
try:
    f = open("demo.txt")
    if f.name == "demo.txt":
        raise Exception
except Exception as e:
    print("Exception")
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally")