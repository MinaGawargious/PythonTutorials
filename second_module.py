import first_module # Whenever we import a module, it runs that code

print(f"Second module's name: {__name__}")
print(f"Calling first module's main method from second_module")
first_module.main()
