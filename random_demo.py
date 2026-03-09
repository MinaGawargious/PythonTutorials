import random # for security or cryptography, use the secrets module

x = random.random() # between 0 (inclusive) and 1 (exclusive). So [0, 1)
print(x)

# To get a number between 2 numbers, we could either multiply (so to get between 0 and 10, multiply x by 10), or use the uniform() method

x = random.uniform(0, 10) # Get random number between 0 and 10, including 0, excluding 10
print(x)

# To get random integers, use randint
x = random.randint(0, 10) # Get random integer between 0 and 10, inclusive of both
print(x)

# The choice method picks a random value from a list of values
greetings = ["Hello", "Hi", "Hey", "Howdy", "Hola"]
greeting = random.choice(greetings) # same as greetings[random.randint(0, len(greetings)-1)]
print(greeting)

# We can get multiple random values from a list via choices() (instead of choice())
multiple_greetings = random.choices(greetings, k=5) # k = # of choices
print(multiple_greetings)

weighted_greetings = random.choices(greetings, weights=[1, 1, 5, 1, 1], k=5) # weights = weighting of each element. "Hey" is 5x as likely as anything else. k = # of choices to pick
print(weighted_greetings)

# We can also shuffle a list of values, like an array 1-52 to represent a deck of cards
deck = list(range(1, 53))
print(deck)
random.shuffle(deck) # in-place. Doesn't work for tuples since they are non-mutable (TypeError: 'tuple' object does not support item assignment)
print(deck)

# We can pick cards from the deck. We can't use choices since it can pick the same thing multiple times. We want a unique card each time (1 of 52, 1 of 51, 1 of 50, 1 of 49, 1 of 48, etc). Use sample instead
hand = random.sample(deck, 5) # 5 random unique values
# hand = random.sample(deck, 53) # ValueError: Sample larger than population or is negative
print(hand)