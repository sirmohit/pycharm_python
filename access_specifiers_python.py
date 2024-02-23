# In python we can not make atribute and methods strongly private or protected althouth we can make them private and protected.
# If we create a attribute protected or private then it is the developers responsibility to keep it functionaly as it is.
# In Python we use "_" for protected access spcifier and "__" for private access specifier)
#

#Example of Publid access specifier
'''class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Hi myself {self.name} from student class")
s1  = Student("Mohit")
print(s1.name)
s1.display()'''

# PROTECTED SPECIFIER
'''class Student:
    def __init__(self,name,rollno):
        self.name = name
        self._rollno=rollno # here "_rollno" is a protected attribute
    def display(self):
        print(f"Hi myself {self.name} from student class and my roll no is {self._rollno}")
class Branch(Student):
    pass
s1  = Branch("Mohit",38)
print(s1.name)
s1.display()
def publicMethod():
    b1 = Branch("Mohit",38)
    print(b1.name)
    print(b1._rollno) # AS you can see here we can access the protected attribute from public method.
    b1.display()
publicMethod()'''

# PRIVATE SPECIFIER
class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._rollno=rollno # here "_rollno" is a protected attribute
        self.__age = age #here "__age" is private attribute
    def __display(self): # here method is private
        print(f"Hi myself {self.name} from student class and my roll no is {self._rollno} and I am {self.__age} years old")
    def displayPrivateData(self):
        self.__display()

b1 = Student("Mohit",12,21)
#b1.displayPrivateData() # hre we can see that we can access private memberss of class also
# We can access private data using "data mangling" using "dir" function
print(dir(b1))
print(b1._Student__age)# now you can access "age' which is privte attribute
b1._Student__display() #now you can access "display' which is privte method