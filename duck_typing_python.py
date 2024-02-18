# dynamic typing : In dynamic typing we need not to specify the data type at the compile time it will assume it at runtime time by itself according to given value
# In the given example the method use to predict the datatye of value at runtime and returning the valie accodingly
'''def square(x):
    return x*x
print(square(4))
print(square(23.34))'''

#static typing:In static typing we need to ensure the datatype at compile time like in java.
'''static int square(int a){
     return a*a
   }'''

#Duck Typing
class Duck:
    def swim(self):
        print("I can swim")
    def speak(self):
        print("Quack Quack")
class Dog:
    def swim(self):
        print("I am dog and I can swim")
    def speak(self):
        print("woof woof")
class Person:
    def speak(self):
        print("blah blah blah")
def display(obj):
    obj.swim()
    obj.speak()
    print("Information Display",'\n')
d = Duck()
display(d)

d1 =Dog()
display(d1)

p = Person()
display(p)