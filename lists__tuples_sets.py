# lists are sequential data
# sets are unordered collections of values with no duplicates

courses = ["History", "Math", "Phyiscs", "CompSci"]
print(courses)
print(len(courses))
print(courses[2]) # Physics
print(courses[-1]) # Last item
# print(courses[4]) # error
print(courses[0:2]) # [0, 2). This is called slicing, exactly like strings

courses.append("Art")
print(courses)
courses.insert(2, "Spanish") # Insert at index 2, after History and Math
print(courses)
# courses.extend("Test") # Adds 'T', 'e', 's', 't'. Arg is treated as a list
courses.extend(["Test1", "Test2"]) # Desired behavior
print(courses)

courses.remove("Math") # Error if "Math" not in list
print(courses)
popped = courses.pop()
print(popped, courses) # Pops off Test2

courses.reverse() # in-place
print(courses)

courses.sort(reverse=False) # reverse is default False. sort is in-place
print(courses)

print(sorted(courses, reverse=True))
print(courses) # Unchanged since sorted is a function, not a list method

print(courses.index("CompSci")) # error if not in list

for index, item in enumerate(courses, start=1):
    print(index, item)
    
course_str = " - ".join(courses)
print(course_str)
print(course_str.split(" - ")) # original list again

courses2 = courses
print(courses, courses2, id(courses) == id(courses2))

courses[0] = "Changed"
print(courses, courses2) # BOTH changed. They both point to same object in memory

# We can not modify tuples. They are immutable. Lists are mutable

tuple1 = ("History", "Math", "Phyiscs", "CompSci")
tuple2 = tuple1
print(tuple1, tuple2)

# tuple1[0] = "ChangedTuple" # TypeError: 'tuple' object does not support item assignment

print(tuple1, tuple2)

# Sets are unordered and have no duplicates
set1 = {"History", "Math", "Phyiscs", "CompSci", "Math"}
print(set1) # Only 1 Math course. 
print("Math" in set1) # Membership test much faster with sets than lists

set2 = {"History", "Math", "Art", "CompSci", "Math"}
set2.add("Hi")
print(set1.intersection(set2)) # What is in both set1 AND set2. AND operator
print(set1.difference(set2)) # "Physics" was in set1 but not in set2
print(set1.union(set2)) # What is in either. OR operator

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # dict, not set
# empty_set.add("Hi") # Will not work. {} is empty dict. Must declare with set()
empty_set = set() # Correct


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
# []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters_copy = letters # Same address. In C, lists are pointers, so this is like C copying pointers
letters_copy[0] = "Z"
letters_copy[2:4] = ["h", "i"]
print(letters, letters_copy) # Same

letters_slice_copy = letters[:]
letters_slice_copy[0] = "W"
print(letters, letters_copy, letters_slice_copy) # letters and letters_copy are the same. letters_slice_copy is a new memory area entirely
print(id(letters) == id(letters_copy), id(letters) == id(letters_slice_copy)) # True, False