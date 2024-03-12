# OOPS in Python :-

class Demo:  # class defined
    a = 10


obj = Demo()  # object of class
print(obj.a)  # calling variable of class
obj1 = Demo()  # second object of same class , we can create multiple objects of a class


# functions defined inside class are called methods

class demo2:
    def sumvalue(self):  # one argument is necessary
        print(20 + 30)


objdemo = demo2()
objdemo.sumvalue()
