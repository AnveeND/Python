# taking input from user

print("\n-----------------  Taking input   -------------------\n")

print("by default string input so output will be concatenation ")
a = input("Enter the value 1 : ")
b = input("Enter the value 2 : ")
print(a+b)
# By default input is in the form of string
print("Integer input through type casting  ")
a = int(input("a = "))
b = int(input("b = "))
print(a+b)
print()
print("Float input through type casting  ")
a = float(input("a = "))
b = float(input("b = "))
print(a+b)
print()
# eval is used for taking any type of input value
# through eval we can also take input in binary form
a = eval(input("a = "))
b = eval(input("b = "))
print(a+b)
