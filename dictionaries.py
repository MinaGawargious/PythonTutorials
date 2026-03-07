# Dictionaries work with key-value pairs. In other languages, they are called hash maps or associative arrays
# Key is uniuqe identifier, value is the data

student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"], 1: "Hi"}
print(student)
print(student["name"])
print(student[1])
# print(student["non-existant"]) # If key doesn't exist, throw error
print(student.get("non-existant")) # Return None if key doesn't exist
print(student.get("non-existant", "Not Found")) # Return "Not Found" if key doesn't exist

student["phone"] = "555-5555" # If key didn't exist, add it and the value. If it does already exist, update value
print(student["phone"])
student["phone"] = "123-4567" # If key didn't exist, add it and the value. If it does already exist, update value
print(student["phone"])

student.update({"name": "Mina", "age": 27, "phone": "111-1111", "new-key": "test123"})
print(student)

del student["age"]
print(student) # age key deleted

popped = student.pop("phone")
print(popped, student)

print(student.keys(), student.values())
print(student.items()) # dict_items([('name', 'Mina'), ('courses', ['Math', 'CompSci']), (1, 'Hi'), ('new-key', 'test123')])

for item in student.items(): # student.items() is a dict_items object of tuples
    print(type(item)) # tuple
    print(item)
    
for key in student:
    print(key) # JUST the key. Must use .items() method