# Inheritance :-
"""
Parent class methods can be inherited in child class

"""


class A:
    def show(self):
        print("\nClass A ")


class B(A):  # inherited class A in class B
    def disp(self):
        print("\nClass B")


obj = B()  # obj of class B
obj.disp()  # calling method of B with obj of B
obj.show()  # calling method of A with obj of A due to inheritance
