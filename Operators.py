# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Arithmetic Operators
# ---------------------------------

print("\n-------------")

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(b % 3)  # modulus gives the remainder after dividing b by 3
print(5 ** 2)  # square of 5
print(5 ** 3)  # cube of 5 i.e 5*5*5
print(10 / 3)
print(10 // 3)  # Floor Division returns the numbers before point

# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Assignment Operators
# ---------------------------------

print("\n-------------")

x = 5
print(x)

x += 5  # x=x+5
print(x)

x -= 6  # x=x-6
print(x)

# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Comparison Operators
# ---------------------------------

print("\n-------------")

r = 200
q = 200
y = 300

print(r == q)
print(r == y)
print(r != q)
print(r != y)
print(r > y)
print(y > q)
print(r < y)
print(r >= q)


# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Logical Operators
# ---------------------------------

print("\n-------------")

# and -- x<5 and x<10
# or  -- x<5 or x<4
# not -- not(x<5 and x<10)      -- Reverse the result

print(r == q and r < 200)
print(r == q or r < 200)
print(r == 200 and q == 200 and r == q)
print(r == 200 and q == 200 and y > 500)
print(r == 200 or q == 200 or y > 500)
print()
print(x != 10)
print(not x != 10)

# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Membership Operators
# ---------------------------------

print("\n-------------")

# IN      -- present in the list or tuple
# NOT IN  -- Not present in the list or tuple

s = "Hello"

print('H' in s)
print('h' in s)  # False as python is case sensitive
print('h' not in s)

# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Identity Operators
# ---------------------------------

print("\n-------------")

# is  --- Returns true if both variables are the same objects
# is not --- Returns true if both the variables are not the same objects

print(r is q, r == q)
print(r is not q)

# ---------------------------------------------------------------------------------------------------------
# Topic 4 --> Bitwise  Operators
# ---------------------------------

print("\n---------")

# 0 = false
# 1 = True

# & -- And
# | -- OR
# ^ -- XOR

x = 10
y = 8

# bin() is used to calculate the binary of any integer

print(bin(x))
print(bin(y))
print(x & y, bin(x & y))
print(x | y, bin(x | y))
print(x ^ y, bin(x ^ y))


