print(f"First module's name: {__name__}")

def main():
    print("First module's main. Ran directly unless calling first_module.main() from other module")

if __name__ == "__main__": # Is this file being run directly by Python or is it being imported?
    main()
else: # TODO: Can we see WHICH module imported this one?
    print("Imported first_module")
    
# When Python runs a file, before running any code, it sets a few variables, including __name__. When Python runs file directly, __name__ is __main__. If we IMPORT a file instead,__name__ of imported file is that file's name, and name of file we ran directly is __main__