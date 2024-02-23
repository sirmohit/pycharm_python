
#abstract class is class whick is having at least one abstract method and cannot create the object of abstract class.
from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod # its a decorator to make a method abstract
    def start(self):
        pass
    def display(self):
        print("I am concrete method")