f = open("demo.txt", mode="r") # if we don't pass in a mode, it defaults to r for reading
print(f.name, f.mode)
f.close() # If we don't explicity close the file, we may have leaks that cause us to run over the max number of file descriptors allowed on our system, and we may lock the file for other programs (or even our own)

# Better way so we don't have to explicity close the file. Use a context manager
with open("demo.txt", "r") as f2: # Once we exit with block, file gets closed automatically, even if there is an exception or something
    print(f2.name, f2.mode)
    f_contents = f2.read()
    print(f_contents)
    f_lines = f2.readlines() # Empty. Once we go through file once, we can't go through it again here for some reason
    print(f_lines)
    
print(f2, f2.name, f2.mode) # We still have access to f2 variable even after exiting context manager. File will just be closed
# print(f2.read()) # ValueError: I/O operation on closed file.
    
with open("demo.txt", "r") as f3:
	f_lines = f3.readlines() # Get all lines into an array
	print(f_lines)
 
with open("demo.txt", "r") as f4:
	f_contents = f4.readline() # Get 1 line, move pointer to next line
	print(f_contents, end="") # first line
 
	f_contents = f4.readline() # Get 1 line, move pointer to next line
	print(f_contents, end="") # second line
    
# For big files, instead of doing f.read() to get all the content, or f.readlines() to get array of each line do this or f.readline() to get 1 line at a time and move on to the next line:
with open("demo.txt", "r") as f5:
    for line in f5: # We could also do a loop with f.readline() too
        print(line, end="")
    # empty after: once we go through file, future reads are empty. We are at end of file
    print(f5.readline())
    print(f5.readline())
    print(f5.readline())
    print(f5.readline())
    print(f5.readline())
    print(f5.readline())
    
# with f.read(), we can pass in size as argument and specify amount of data to read in:
with open("demo.txt", "r") as f6:
    f_contents = f6.read(100) # read 100 characters from file
    print(f_contents)
    f_contents = f6.read(100) # read 100 MORE characters from file where we left off
    print(f_contents)
    
    f_contents = f6.read(100) # Reached EOF, so empty file returned
    print(f_contents)
    
with open("demo.txt", "r") as f7:
    size_to_read = 10
    f_contents = f7.read(size_to_read)
    print(f"Current position in file is {f7.tell()}")
    
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f7.read(size_to_read)
    print()
        
with open("demo.txt", "r") as f8:
    size_to_read = 10
    f_contents = f8.read(size_to_read)
    f8.seek(0) # Set position back to 0
    print(f_contents, end="*")
    f_contents = f8.read(size_to_read)
    print(f_contents)
    
# with open("demo.txt", "r") as f9:
#     f9.write("will fail due to being open in read mode") # io.UnsupportedOperation: not writable

with open("demo2.txt", "w") as f9: # If file doesn't exist, create it. If it does exist, overwrite it
    f9.write("Test")
    f9.write("Test2")
    f9.seek(0)
    f9.write("Writing at beginning") # Overwrites as many characters as it needs to
    
with open("demo.txt", "r") as rf:
    with open("demo_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)
            
with open("demo.txt", "r") as rf, open("demo_copy2.txt", "w") as wf: # also works
        for line in rf:
            wf.write(line)
            
# Copying images and other binary files:
with open("kitty.jpeg", "rb") as rf:
    with open("kitty_copy.jpeg", "wb") as wf:
        for line in rf:
            wf.write(line)
# TODO: What exactly does "reading as binary" mean, why is it different from reading text, and look into utf-8 codec encoding

with open("kitty.jpeg", "rb") as rf:
    with open("kitty_copy2.jpeg", "wb") as wf:
        chunk_size = 4096
        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)