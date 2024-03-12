# ERRORS :-
"""
- Two types:-
    1)Syntax errors - which cannot be handled
    2)Logical errors - also called as exceptions which can be handled
                        for example :-
                            print(1/0)  division by zero error

- exception handling is nothing but continuing the program execution even if any logical error occurs.
- type of exceptions :
                            1) ZeroDivisionError --> Dividing a number by zero
                            2) NameError --> using variable without defining [print(x)  value of x is not assigned]
                            3) TypeError --> concatenating string and a number
                            4) ValueError --> Entering value of different datatype than that in which the variable was defined
                            5) IndexError --> accessing index of list out of its range
                            6) KeyError --> different key rather than defined key is accessed in a dictionary
                            7) ModuleNotFoundError --> using module which is not defined
                            8) ImportError --> calling function which is not defined in the module

"""
# Handling exceptions : - using 'try' and 'except' :-

l1 = [2, 4, 5, 7]
# print(l1[4])    --> IndexError: list index out of range
try:
    print(l1[4])
except:
    print("\nError occured ")  # prints 'Error occured' and executes rest of code

# Using buit-in exceptions :-
try:
    print(l1[5])

except IndexError as e:
    print(e)  # list index out of range

# finally - code under finally block is always executed

finally:
    print("\nthis is finally block , this is always executed ")
