# User defined functions :-
# -----------------------------------

# Simple function :-
def simple_func():
    print("\nThis is simple function ")


# Function with arguments :-
def adding(a, b):
    print("\nAdding a and b through function with arguments --> a+b = ", a + b)


# Function calls -->

simple_func()

# Taking input from user for adding
n1 = int(input("\nEnter n1 = "))
n2 = int(input("\nEnter n2 = "))
adding(n1, n2)


# arguments with default values -->
def sumofno(x, y=4):  # default value is set for y
    print()
    print(x + y)


sumofno(n1)


# Return in function -->
def SUM(a, b):
    c = a + b
    return c


print()

s = SUM(n1, 30)
print(s)
