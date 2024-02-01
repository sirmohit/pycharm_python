'''class pwskills:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def stu_details(self):
        print(self.name,self.email)
pw = pwskills("Mohit","mohit@gmail.com")
print(pw.name)
print(pw.email)
pw.stu_details()'''

'''class pwskills1:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    @classmethod
    def classMethod(cls,name,email):#class method :this is use to overload the "init" and know we can pass the arguments directly to this method and call it without making the object of the class
        return cls(name,email)
    def stu_details(self):
        print(self.name,self.email)
pw=pwskills1.classMethod("Mohit","Mohit@gmail.com")
print(pw.name)
print(pw.email)
pw.stu_details()# we can even call any method of the class class directly by class method variable'''

'''class pwskills2:
    mobile_no = 123234234 # class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
    @classmethod
    def change_number(cls,mobile):#this method change the mobile number directly while calling the method
        ws= pwskills2.mobile_no = mobile
        return ws

    @classmethod
    def classMethod(cls, name, email):  # class method :this is use to overload the "init" and know we can pass the arguments directly to this method and call it without making the object of the class
        return cls(name, email)

    def stu_details(self):
        print(self.name,self.email,pwskills2.mobile_no)# accessing the mobile number into a method
print(pwskills2.change_number(2134565423))
pw = pwskills2.classMethod("adfad","adfa@gmail.com")
pw.stu_details()
pw.name
pw.email'''

class pwskills3:
    mobile_no = 123234234 # class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
    @classmethod
    def change_number(cls,mobile):#this method change the mobile number directly while calling the method
        ws= pwskills3.mobile_no = mobile
        return ws

    @classmethod
    def classMethod(cls, name, email):  # class method :this is use to overload the "init" and know we can pass the arguments directly to this method and call it without making the object of the class
        return cls(name, email)

    def stu_details(self):
        print(self.name,self.email,pwskills3.mobile_no)# accessing the mobile number into a method
# how involve the out side method add into a class which is not a part of class
def course_details(cls,course_name):
    print("course name is ",course_name)
pwskills3.course_details = classmethod(course_details)# attaching external function into our existing class
pwskills3.course_details("data science master")

def mentor(cls,list_of_mentor):
    return list_of_mentor
pwskills3.mentor = classmethod(mentor)
print(pwskills3.mentor(["sudh","krish"]))

#deleting the function
del pwskills3.change_number #way1

delattr(pwskills3,"stu_details")

delattr(pwskills3,"mentor")

delattr(pwskills3,"mobile_no")




