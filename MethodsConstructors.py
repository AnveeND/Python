# Methods and Constructors :-
"""
No need to call a constructor
constructor is automatically called when object of a class is created
method needs to be called with the help of object of a class

"""


class newclass:
    a = 10

    def __init__(self):                            # this is a constructor , it is always defined with ' __init__ '
        print("\nThis is a constructor ")

    def show(self):
        """ print("\na = ", a)                      --> NameError: name 'a' is not defined ( We need to use self to access a) """
        print("\na = ", self.a)

    def adds(self):
        c = self.a + 30
        print(c)

    def para(self, a, b):  # parameters need not to accessed with the help of self
        print("\nParameterized function : \na is ", a, "\nb is ", b)


obj = newclass()                  # constructor called
obj.show()
obj.adds()
obj.para(20, 30)  # calling parametrized function and no need to pass argument for self
