# Polymorphism : -
"""
- Overloading and overriding
- polymorphism means same function name but different signatures (definitions) being used for different types
- for example len() function : it is used to count length of lists as well as strings
"""

l = [4, 9, 0, 7, 6]
s = "WELCOME"
print("\nList length ", len(l))
print("\nString length ", len(s))

# OVERLOADING :-
"""Same function with different parameters can be used """


class over:
    def display(self, name=''):
        print("\nWelcome ", name)

    def newinfo(self):
        print("\nnewinfo in over class ")


obj = over()
obj.display()  # without parameter passing
obj.display("RIYA")  # same function with parameter passing


# OVERRIDING :-

class Ride(over):
    def newinfo(self):
        super().newinfo()  # used to call function of parent class of same name
        print("\nnewinfo in Ride class ")


o1 = Ride()
o1.newinfo()  # newinfo in Ride class  --> function of class Ride overrides the function of class over


# Overloading example :-
class Area:
    def findar(self, a=None, b=None):
        if a is not None and b is not None:
            print("\nArea is : ", a * b)
        elif a is not None:
            print("\nArea is ", a * a)

        else:
            print("\nArea is zero ")


newobj = Area()
newobj.findar()         # same method with no arguments
newobj.findar(12)       # same method with one argument
newobj.findar(23, 24)   # same method with two arguments



