# Multilevel inheritance :- inheriting a child class

class A:
    a = 10
    b = 200

    def printing(self):
        return self.a + self.b


class B(A):

    def value(self):
        print("a is : ", self.a)  # Accessing variable of class A
        print("b is : ", self.b)


class C(B):  # inherited class B  but also can access functions of class A as it is inherited by B
    def new(self):
        self.value()
        print("\nClass C a and b are :  ", self.a, " ", self.b)


obj = C()
k = obj.printing()   # Accessed class A method with help of class C obj
print(k)
obj.new()
