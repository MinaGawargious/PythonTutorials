message1 = "double quotes"
message2 = 'single quotes'
# message3 = 'error's quotes
message4 = 'no error\'s quotes' #escape character \
message5 =  r"raw string mean\"s we print literally" # will print the \ and the " literally. r = raw string
message6 = """multi
line
text"""
message6 = """2\
line\
text
here""" # \ at end of line prevents new line

print("2 or more string LITERALS (not variables) next to each other" " are automatically concatonated"
      " useful for multi-line strings like this")


print(message1)
print(message2)
# print(message3)
print(message4)
print(message5)
print(message6)

print(len(message1)) # 13
print(message1[3]) # print b
print(message1[-10]) # print b (count from end starting at -1)
print(message1[0:7]) # print double. Includes first index, not last
print(message1[:7]) # print double. Leaving first index = start at 0
print(message1[7:13]) # print quotes
print(message1[7:]) # print quotes. Leaving first index = end at last character (index len(message1))

# This makes sure s[:i] + s[i:] is always equal to s

# print(message1[15]) # out of bounds
print(message1[1:15]) # End out of bounds -> stop at last character, inclusive
print(message1[15:]) # Start out of bounds -> empty string

print(message1.upper())
print(message1.count('u')) # 2 u's in "double quotes"
print(message1.find('u')) # index 2
print(message1.rfind('u')) # index 8 is last u
print(message1.replace('u', 'ayy')) # new string, not in place
print(message1) # double quotes, not doayyble qayyotes
print(message1 + " " + message2) # concatonate. The space is a string literal
print("%s %s" %(message1, message2)) # Same as above, but cleaner format string. C-style
print("{} {}".format(message1, message2)) # Same as above, but cleaner format string
print(f"{message1} {message2}") # Same as above, but even cleaner format string

print(dir(message1)) # All functions available to this variable
print(dir(type(message1))) # All functions available to this variable's type. Idential as above, except when we have custom classes where we add a per-instance attribute
print(help(message1)) # won't work. Need to run it on class, attribute or method
print(help(message1.upper))
print(help(str.upper)) # same as above
print(help(str))

# Note: Python does not have a char type. A character is simply a string of size 1
# Python strings are also immutable
# message1[0] = "a" # TypeError: 'str' object does not support item assignment