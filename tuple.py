# TUPLE :-
"""
ordered , immutable , defined with ()
single element is never considered as a tuple . Tuple should always contain more than one value
"""
t = (20, 30, 40, 50, 60)       # Tuple
print(type(t))
a = ("python")                 # single element, hence it is not a tuple
b = (30)                       # This is also not a tuple
print(type(a))
print(type(b))


# Accessing element from a tuple :-
x = t[3]
y = t[-1]
print(x, " ", y)
print()

# Iteration of tuple :-

# using Range
l = len(t)
for i in range(l):
    print(i, " ", t[i])
print()
# not using range
for i in t:
    print(i)
print("\nTuple is : - \n", t)
print("\nFunctions of tuple :- \n")
# functions in tuple :-
m = min(t)
print("\nmin(t) --> ", m)

mx = max(t)
print("\nmax(t) --> ", mx)

c = t.count(20)                # Counts the number of times particular value is repeated
print("\nt.count(20) -->", c)

ij = t.index(40)               # Returns the index of particular value
# ij1 = t.index(90)              --> ValueError: tuple.index(x): x not in tuple
print("\nt.index(40) -->", ij)

su = sum(t)
print("\nsum(t) --> ", su)     # prints sum of elements in the tuple (don't work if tuple contains strings )
s1 = sum(t, 20)                 # adds 20 in the sum of elements of t  i.e  20 + sum(t) -- (sum = 20 as default)
print("\nsum(t, 20) --> ", s1)
