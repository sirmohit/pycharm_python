'''How to achieve memory optimization
   difference between static menthod ,class method and instance method
   how to call static method in class method, static and instance method'''

'''class pwskills:
    def mentor(self,list_of_mentor):#it called as insance mehod also
        print(list_of_mentor)
pw = pwskills()
pw.mentor(["sudh","krish"])'''

'''class pwskills1:
    def student_detail(self,name,mail_id,number):#I have to make the object ot acess this method
        print(name,mail_id,number)

    @staticmethod
    def mentor(list_of_mentor):# it is a static method and we can call it by class name without making any object
        print(list_of_mentor)

pw = pwskills1()
pw.student_detail("mohit","mohit@gmail.com,",1233423412)

# calling static method
pwskills1.mentor(["sudh","krish"])'''

#case 2 : calling a static method in a class method of any instance mehtod
class pwskills1:
    def student_detail(self,name,mail_id,number):#I have to make the object ot acess this method
        print(name,mail_id,number)
    @staticmethod
    def mentor_mail(list_of_mail):
        pwskills1.mentor(["sudh","krish"])# calling one static method into another
        print(["sudh@gmail.com","krish@gmail.com"])
    @staticmethod
    def mentor(list_of_mentor):# it is a static method and we can call it by class name without making any object
        print(list_of_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor(["sudh","krish"])

    #calling static method in instance method
    def mentors(self,mentor_list):
        print(mentor_list)
        self.mentor_mail(["sudh@gmail.com","krish@gmail.com"])

pwskills1.mentor_mail(["sudh@gmail.com","krish@gmail.com"])

pw = pwskills1()
pw.mentors(["sudh","krish"])

