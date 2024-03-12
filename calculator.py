# calculator program

o = input("Enter the operator of the operation : ")
a = int(input("Enter first no.  : "))
b = int(input("Enter second no.  : "))
if o == '+':
    print("Addition is : ", a+b)
elif o == '-':
    print("Subtraction is : ", a-b)
elif o == '*':
    print("Multiplication is : ", a*b)
elif o == '/':
    print("Division is : ", a/b )
else:
    print("invalid !!!")

