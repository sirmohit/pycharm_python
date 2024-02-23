from abstract_demo import Vehicle

# Python does not support abstraction directly but we can achieve it by using "abc" module import the ABC Class of python.
class Bike(Vehicle):
    def __init__(self,n,color):
        self.no_of_tyres = n
        self.color = color
    def start(self):
        print("start with kick")
class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyres =n
    def start(self,n):
        print("self start")
class Car(Vehicle):
    def __init__(self,n,x):
        self.no_of_tyres = n
        self.no_of_gears = 6
    def start(self):
        print("start with key")