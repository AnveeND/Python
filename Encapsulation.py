# Encapsulation :-
"""
Making variable or method private
An objects variables should not be directly accessible

private variable is defined with : __Var

private variable can only be used inside the class

private method syntax : __methodName(self)

"""


class student:
    __name = "Raja"  # private variable as defined with __varname

    def __disp(self):  # using __ we can define a private method
        print("\nThis is private method ")

        # To access this private variable and method use constructor

    def __init__(self):
        print("\n", self.__name)
        self.__disp()


obj = student()
# print(obj.__name)   --> AttributeError: 'student' object has no attribute '__name' (as it is private variable)
# obj.__disp()          --> AttributeError: 'student' object has no attribute '__disp'  ( as it is a private method)


# Getter and Setter methods :-
"""
used to set values to private variable 
not inbuilt but we have to make them 
to set the value to a private variable we will make a function named setter 
and to get this value we will make a function named getter 
"""


class getset:
    def __init__(self):
        self.__name = ""  # defining blank private variable

    def Getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name


o = getset()   # variable __name is defined
o.setname("Riya")    # Riya is sent to name parameter and is set to __name
name = o.Getname()   # __name is accessed
print(name)
