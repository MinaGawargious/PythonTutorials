nums = [1, 2, 3, 4, 5]

# The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. This is from the documentation. It iterates over an iterable
for num in nums:
    print(num)
    
# Range function and iterables:    

# To iterate over a range, use the range function
for i in range(5): # 0-4
    print(i)
    
for i in range(3, 8): # 3-7
    print(i)
    
for i in range(3, 11, 2): # 3, 5, 7, 9
    print(i)
    
# Note: a range is just a range object, NOT a list. It is an object that returns the successive items of the desired sequence when you iterate over it until the supply is exhausted, but it doesn't make the list itself
# So, the range object is an iterable, which is an object capable of returning its members one at a time. We can create an iterator by passing them to the iter() function, and iterators are good for one pass of the iterable, but it is usually done automatically via a temporary unnamed variable in loops for us already.for loops and the sum() function are examples of constructs that take iterables, which expect something from which they can obtain successive items until the supply is exhausted
print(range(10)) # range(0, 10)

# Break and continue:

for num in nums: # prints 1, 2, Found!
    # break breaks out of innermost loop
    if num == 3:
        print("Found!")
        break
    print(num)
    
for i in range(3): # prints 1, 2, 0 Found! 1, 2, 1 Found! 1, 2, 2 Found!
	for num in nums: 
		# break breaks out of innermost loop
		if num == 3:
			print(i, "Found!")
			break
		print(num)
    
for num in nums: # prints 1, 2, Skipping 3, 4, 5
    # continue moves on to the next iteration of the innermost loop
    if num == 3:
        print("Skipping 3")
        continue
    print(num)
   
for i in range(3): 
	for num in nums: # prints 1, 2, 0 Skipping 3, 4, 5 1, 2, 1 Skipping 3, 4, 5 1, 2, 2 Skipping 3, 4, 5
		# continue moves on to the next iteration of the innermost loop
		if num == 3:
			print(i, "Skipping 3")
			continue
		print(num)
    
# While loops:

x = 0
while x < 10:
    print(x)
    x+=1
    
# Fibbonacci
a, b = 0, 1 # a = 0, b = 1
while a < 10:
    print(a, end=", then ") # Instead of newline, we can override end string to be whatever we want
    a, b = b, a+b # RHS evaluated first from left to right, then assigned to LHS. a gets old value of b, b gets old value of a plus old value of b
    
