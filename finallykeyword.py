# finally keyword :-
# code under finally block is always executed

def func1():
    try:
        l1 = [1, 2, 3, 4, 5]
        i = int(input("\nEnter the index value : "))
        print("\nValue at index ", i, " is ", l1[i])
        return 1
    except:
        print("\nSome error occurred")
        return 0

    # print("\nThis is not under finally block this will not be executed ")
    finally:
        print("\nThis is in finally block so it is always executed ")


x = func1()
print("\nReturned value is : ")
print(x)
