# Sets :-
"""
Unordered , un-indexed , you can add or delete data but cannot change data in sets
defined using set() function or {}
it doesn't have key-value pair
only stores unique elements
"""

s = {20, 30, 40, 30, 10, 30}
print("\nSet is --> ", s)     # prints 30 only once
# can print randomly as it is unordered
print()

for i in s:
    print(i)


# function of sets :-

print()

l1 = [20, 300, 655, 700, 300]
print("l1 is ", l1)
s1 = set(l1)                     # Converts list to a set
print("\nset(l1) --> ", s1)

s.add(350)                       # adds the element to the set
print("\ns.add(350) --> ", s)

s.pop()                          # pops random element from set
print("\ns.pop() --> ", s)
print("\nprint(s.pop) --> ", print(s.pop))

s.remove(20)                     # removes specific element but raises an error if element is not present in the set
print("\ns.remove(20) --> ", s)

s.discard(350)                   # removes specific element do not raise error if element is not there in set
print("\ns.discard(350) --> ", s)

s.clear()                        # removes all elements from set and returns set() so as to differentiate between blank set and dictionary
print("\ns.clear() --> ", s)

l2 = [2, 3, 4, 5, 6]
s1 = {2, 1, 7, 8, 9, 0}
s1.update(l2)                    # Adds multiple elements keeping only unique elements in updated set
print("\nl2 --> ", l2, "         s1 --> ", s1)
print("\ns1.update(l1) --> ", s1)
