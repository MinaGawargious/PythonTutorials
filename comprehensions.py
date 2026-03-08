# List comprehensions are easier and more readable ways to make a list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want n for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list2 = [n for n in nums] # list comprehension is so much cleanier and easier to read
print(my_list2)

# I want n*n for each n in nums
my_list3 = []
for n in nums:
    my_list3.append(n*n)
print(my_list3)

my_list4 = [n*n for n in nums]
print(my_list4)

# Using a map + lambda
# map runs everything in list through a function, and lambda is a function
my_list5 = list(map(lambda n: n*n, nums))
print(my_list5)

# I want n for each n in nums if n is even
my_list6 = []
for n in nums:
    if n%2 == 0:
    	my_list6.append(n)
print(my_list6)

my_list7 = [n for n in nums if n%2 == 0]
print(my_list7)

# Can also use filter + lambda. It filters based on a function condition:
my_list8 = list(filter(lambda n: n%2 == 0, nums))
print(my_list8)
# TODO: Dig deeper into maps, filters and lambdas

# I want a (letter, num) pair for each letter in "abcd" and each number in "0123"
my_list9 = []
for letter in "abcd":
    for num in range(4):
        my_list9.append((letter, num))
print(my_list9)

my_list10 = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list10)

# Dictionary comprehensions:
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

# I want a dict{"name": "hero"} for each name, hero in zip(names, heroes)
my_dict = {}
for name, hero in zip(names, heroes): # zip matches names 1 to 1 based on index, based on smaller of 2 lists
    my_dict[name] = hero
print(my_dict)

my_dict2 = {name: hero for name, hero in zip(names, heroes)} # dictionary comprehension
my_dict3 = dict(zip(names, heroes)) # easier imo
print(my_dict2)
print(my_dict3)

my_dict4 = {name: hero for name, hero in zip(names, heroes) if name != "Peter"} # dictionary comprehension with a conditional. Easier than if statement inside a for loop
print(my_dict4)

# Set comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set) # removed duplicates. Only unique values

my_set2 = {n for n in nums}
my_set3 = set(nums) # easier imo

print(my_set2)
print(my_set3)

# Generator expressions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def gen_func(nums):
    for n in nums:
        yield n*n
        
my_gen = gen_func(nums)

for i in my_gen:
    print(i)
    
my_gen2 = (n * n for n in nums) # not a tuple
for i in my_gen2:
    print(i)
    
print(type(my_gen), type(my_gen2))

# TODO: Review generators