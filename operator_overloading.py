'''print(1 + 2)
print('1'+ '2')
print(int.__add__(1,2))
print(str.__add__('1','2'))'''

# adding two complex number using operator overloading
'''class ComplexNumber:
    def __init__(self,r,i):
        self.real = r
        self.imag = i
    # now we define our own add method to overload the opetrator
    def __add__(self,other):
        return f"{self.real+other.real} + {self.imag + other.imag}i"
c1 = ComplexNumber(12,4)
c2 = ComplexNumber(2,3)
print(c1 + c2)'''

# Overloading the ">" operator
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Ram",23)
p2 = Person("Rahul",24)
if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
