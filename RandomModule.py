# RANDOM MODULE :-
# basically used to get random values

import random

# randint(a , b) --> Gives a random integer between the range a ,b (both included)
n = random.randint(2, 8)
print("\nrandom.randint(2, 8) --> ", n)


# randrange(a, b) --> Gives a random integer between the range a ,b (a included , b not included)
n1 = random.randrange(4, 6)
print("\nrandom.randrange(4, 6) --> ", n1)


# choice() --> Returns a random element from a list
l1 = [19, 10, 30, 40]
ch = random.choice(l1)
print("\nList --> ", l1)
print("\nrandom.choice(l1) --> ", ch)


# random() --> Returns a random float value between 0 and 1
r = random.random()
print("\nrandom.random() --> ", r)


# shuffle() --> Takes a sequence and returns the sequence in random order
ll = [10, 5, 6, 33, 88, 100]
print("\n List is --> ", ll)
random.shuffle(ll)
print("\nrandom.shuffle(ll) --> ", ll)

# uniform() --> Returns a random float no. between two given parameters
u = random.uniform(3, 9)
print("\nrandom.uniform(3, 9) --> ", u)
