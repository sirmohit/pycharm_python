# Python do not support "method overloading" but we can achieve it through some ways
# Mehthod Overloading is used to achieve runtime polymorphism,it occurs in same class with different parameters
'''class Demo:
    def add(self,a,b):
        return a+b
    def add(self,a,v,c):
        return a+v+c
d = Demo()
print(d.add(12,34))# it will give error
print(d.add(12,3,34))'''

# Method Overloading using default argument
'''class Demo:
    def add(self,a,b,c=0):#here c =0 is default args
        return a+b+c
d = Demo()
print(d.add(12,34))
print(d.add(12,3,34))'''

#Method overloading through varible args(*args)
'''class Demo:
    def add(self,*args):# *args will take variable argument pass to the method
        total = 0
        for i in args:
            total = total +i
        return total
d = Demo()
print(d.add(12,34))
print(d.add(12,3,34))
print(d.add(12,23,34,45,56))'''

#METHOD OVERRIDING :Method overriding is used to achieve runtime polymophisims,methods are in different class,methods must have same name and same parameter
class Father:
    def sleep(self):
        print("Father sleeps 10:00 PM to 5:00 AM")
    def eat(self):
        print("He takes health food")
class Son(Father):
    def sleep(self):
        print("No fix time of sleeping")
        super().sleep()
s = Son()
s.sleep()

