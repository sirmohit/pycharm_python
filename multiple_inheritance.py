class Human:
    def __init__(self,heart):
        print("I am in human class")
        self.heart  = heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can do any work")
class Male:
    def __init__(self,name):
        print("I am in Male class")
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")#if two method with the same name are define in two class in multiple inhritance then the child class which id used to inherit the class by sequence
class Boy(Human,Male):#it will call the Human word method
    def __init__(self,name,language,heart):
        self.lan = language
        Human.__init__(self,heart)
        Male.__init__(self,name)
    def work(self):
        print("I can test")
        super().work()
obj1 = Boy("Mohit","java",1)
#obj1.work()##it will call the Human word method
#Male.work(obj1)#now it will call the "work" method of Male class
#obj1.work()

# NOw we can access the constructor of both the parent calsses using the child class
print(obj1.name,obj1.heart,obj1.lan)# At the time of calling attribute name should be same don't use name of positional args