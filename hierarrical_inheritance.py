# In hierarical inheritace one parent class is used to inherited by more than one child class and there is not relation beween child classes
class Human:
    def __init__(self,name,age):
        print("I am in human class")
        self.name = name
        self.age = age
        self.profession = "Engineer"
    def eat(self):
        print("I can eat")
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def __init__(self,name,age):
        print("I am in Female class")
        Human.__init__(self,name,age)
        super().__init__(name,age)
    def work(self):
        print("I can word like human")
female = Female("Mohan",23)
print(Female.mro()
)
'''female.work()
female.eat()
Male.sleep(female)#accessing the male class
male = Male()
male.eat()
male.sleep()
Female.work(male)'''

print(f"My name is{female.name} and I am {female.age} year old")
