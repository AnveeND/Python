# Multiple inheritance :- two or more classes inherited by a single class

class A:
    a = 10
    b = 200

    def printing(self):
        return self.a + self.b


class B:
    c = 500

    def value(self):
        print("c is : ", self.c)


class C(A, B):  # inherited both the classes A and B
    def new(self):
        self.value()  # called function of inherited class B


obj = C()  # object of child class C
x = obj.printing()  # Called function of class A through object of class C
print(x)
obj.new()   # called function of C
print(obj.a)  # Accessing variable of parent class through object of child class

