import math

# ceil() --> returns the smallest integer greater than the given value
#            ceiling of the passed value

x = 10.2
print(math.ceil(x))
y = 10
print(math.ceil(y))        # No changes for integer values


# fabs() --> Returns absolute value i.e if x is negative it returns positive x
a = -9
print(math.fabs(a))


# factorial() --> Returns the factorial of the value  (raises the error if given value is negative or non integer)
b = 5
print(math.factorial(b))
""" ------- Main logic behind factorial ----------
  
fact = 1
for i in range(1, b+1):
    fact = fact*i

print(fact)
"""

# floor --> displays nearest integer less than given value i.e displays no. before point
print(math.floor(44.8))


# fsum --> Returns accurate floating point sum of values in iterable i.e lists or tuples
l = [2, 4, 5, 6, 7]
print(math.fsum(l))


# sqrt --> returns the square root of the number
print(math.sqrt(9))
print(math.sqrt(5))
