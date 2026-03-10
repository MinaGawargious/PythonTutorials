# Generators:
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums) # [1, 4, 9, 16, 25]

def square_numbers_generator(nums):
    for i in nums:
        yield (i*i) # yield keyword is what makes it a generator. More readable, less memory, on-demand results

my_nums = square_numbers_generator([1, 2, 3, 4, 5])
print(my_nums) # <generator object square_numbers_generator at 0x7bbb96f6a570>
# Generators don't hold entire result in memory. It yields 1 result at a time, and waits for us to ask for next result. This saves memory, and let's say we don't need all the numbers in our code (we have some condition that is met early in the sequence), we save time not creating the entire list. Every generator is an iterator
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) # StopIteration exception

# We can still use loops with generators
for i in my_nums:
    print(i)
    
# List comprehension:
my_nums = [x*x for x in [1, 2, 3, 4, 5]] # list
print(my_nums)

my_nums = (x*x for x in [1, 2, 3, 4, 5]) # generator
print(my_nums)
print(list(my_nums)) # Get all values