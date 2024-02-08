class A:
    def display(self):
        print("I am in class A")
class B(A):
    def display(self):
        print("I am in class B")
class C:
    def show(self):
        print("HI I am from class C")
class D(B,C):
    def display(self):
        print("I am in  class D")
objd = D()
print(D.mro())
objd.show()
objd.display()