# stack using list
stack = []
print("-----------------  Perform stack operations --------------------- ")

while True:
    print("\n--------------------------------\n1) Push element\n2) Pop element\n3) Peek element\n4) Display stack\n5) Exit Program\n-------------------------------- ")
    ch = int(input("\nEnter the no. of operation of your choice : "))

    if ch == 1:
        no = int(input("How many elements do you want to enter : "))
        for x in range(no):
            a = int(input("Enter element no. " + str(x+1) + " : "))
            stack.append(a)



    elif ch == 2:
        if len(stack) == 0:
            print("\nStack is empty !! ")
        else:
            k = stack.pop(-1)
            print("\nElement removed form stack is : ",k)

    elif ch == 3:
        if len(stack) == 0:
            print("\nStack is empty !! ")
        else:
            print("\nRecently entered element in the stack is : ", stack[-1])
    elif ch == 4:
        print("\n", stack)

    elif ch == 5:
        print("\nThanks for using stack ")
        break

    else:
        print("\n\tTry again !!")


