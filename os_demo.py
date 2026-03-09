# os module lets us interact with underlying operating system. We can navigate file system, get file info, lookup and change env vars, move stuff around, etc.
import os

print(os.getcwd())
os.chdir("/mnt/c/Users/MinaG/")
print(os.getcwd())
os.chdir(os.getcwd() + "/..")
print(os.getcwd())

print(os.listdir()) # List files in directory. We can pass in directory, or by default use cwd
os.chdir("/mnt/c/Users/MinaG/Python Tutorials")
# We can create a folder via os.mkdir or os.makedirs(). If we want to create a folder a few levels deep, os.makedirs() will create the intermediate levels and os.mkdir() won't
# os.mkdir("OS-Demo-2/Sub-Dir-1") # FileNotFoundError: [Errno 2] No such file or directory: 'OS-Demo-2/Sub-Dir-1'
os.makedirs("OS-Demo-2/Sub-Dir-1")
print(os.listdir())

# os.rmdir("OS-Demo-2/Sub-Dir-1") # Will not remove intermediate directories
os.removedirs("OS-Demo-2/Sub-Dir-1") # WILL remove intermediate directories
print(os.listdir())

# Renaming a file or folder:
# os.mknod("test.txt") # make new file
# os.rename("test.txt", "demo.txt")

demo_stat = os.stat("demo.txt")
print(demo_stat)
from datetime import datetime
print(demo_stat.st_mtime) # Get the modified time
print(datetime.fromtimestamp(demo_stat.st_mtime)) # Get the modified time in human-readable format

# Get entire directory tree and files within desktop. Traverse directory tree and print directories and files via os.walk()
# os.walk() is a generator that yields a 3-value tuple as it's walking directory tree: (directory path, directories within that path, files within that path)
print(os.walk(os.getcwd()))

# for (dirpath, dirnames, filenames) in os.walk(os.getcwd()): # DFS
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
    
print(os.environ) # Prints out all environment variables as a dictionary-like structure
print(os.environ["HOME"]) # Prints out all environment variables

# We can create a correct path by concatenating, but it might change per-os. Instead, use os.path.join

file_path = os.path.join(os.environ["HOME"], "new_file.txt")
print(file_path)

with open(file_path, "w") as f:
    f.write("testing 123")
    
print(os.path.basename("/tmp/dir2/test.txt")) # prints out test.txt, which is the filename
print(os.path.dirname("/tmp/dir2/test.txt")) # prints out /tmp/dir2, which is the dirname
print(os.path.split("/tmp/dir2/test.txt")) # prints out ('/tmp/dir2', 'test.txt'), which is the both dirname and filename

print(os.path.exists("/tmp/dir2/test.txt")) # Check existance of path
print(os.path.isdir("/home/minagawargious")) # Check if something is a directory
print(os.path.isfile("/home/minagawargious/new_file.txt")) # Check if something is a file

print(os.path.splitext("/home/minagawargious/new_file.txt")) # Split path and extension. So here, return ('/home/minagawargious/new_file', '.txt')

print(dir(os.path))