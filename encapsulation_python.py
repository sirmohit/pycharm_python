# Use "getters" and "setter" to avoid direct access of private data
class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._rollno=rollno # here "_rollno" is a protected attribute
        self.__age = age #here "__age" is private attribute
    def get_age(self):# getter method to get the data
        return self.__age
    def set_age(self,age):#setter method to modify data
        self.__age = age
    '''def __display(self): # here method is private
        print(f"Hi myself {self.name} from student class and my roll no is {self._rollno} and I am {self.__age} years old")
    def displayPrivateData(self):
        self.__display()'''
s1 = Student("Mohit",12,32)
print(s1.get_age()) #calling get method
s1.set_age(23) # calling set method and modifing the private data
print(s1.get_age())
