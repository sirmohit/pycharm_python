class Human:
    can_breath = True
    def __init__(self,name):
        self.na = name
        print(f"My name is {name}")
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def sleep(self):
        print("Take sleep of 8 hours")
class Boy(Male):
    def __init__(self,name):
        Human.__init__(self,name)
    def play(self):
        print("I play cricket")
    def work(self):
        # calling method of parent class which is being overrinden in child class by two ways
        Human.work(self) # first way
        super().work() #secod way
        print("I use to code")
obj = Boy("Mohit")
print(Boy.mro())
obj.work()
obj.na
print(obj.can_breath)