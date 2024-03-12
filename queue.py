# queue using list

q = []

while True:
    print(
        "\n------------------------\n1) Enqueue\n2) Dequeue\n3) Front element\n4) Rear element\n5) Display\n6) Exit\n----------------------\n  ")
    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        n = int(input("\nHow many elements do you want to add : "))
        for i in range(n):
            a = int(input("\nEnter " + str(i + 1) + " Element : "))
            q.append(a)

    elif ch == 2:
        if len(q) == 0:
            print("\nQueue is empty !!!! ")
        else:
            v = q.pop(0)
            print("\nElement removed is ", v)
    elif ch == 3:
        if len(q) == 0:
            print("\nQueue is empty !!!! ")
        else:
            print("\nFront element is ", q[0])

    elif ch == 4:
        if len(q) == 0:
            print("\nQueue is empty !!!! ")
        else:
            print("\nLast element is ", q[-1])

    elif ch == 5:
        print("\nThe queue is : ", q)

    elif ch == 6:
        print("\nThanks !!")
        break

    else:
        print("\n\tTry again !!!")
