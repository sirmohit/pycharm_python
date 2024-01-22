class Human:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("I can eat")
    def work(self):
        print('I do code')
class Male(Human):
    def __init__(self):
        super().__init__("mohit")# calling the parent init method to access though child class
        self.no_eye = 2
        self.no_nose = 1

    def flirt(self):
        print("I can flirt")
    def work(self):# method overriding
        super().work() # calling the method of parent class
        print("I can run")
obj_1 = Male()
obj_1.work()
obj_1.flirt()
print(obj_1.no_eye)
print(obj_1.no_nose)
print(obj_1.name)