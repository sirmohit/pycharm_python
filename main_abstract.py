#calling file : here you call all method by hiding their implimentation
from main import *
print("About bike")
bike = Bike(2,"Black")
print(bike.color)
bike.start()
print(bike.no_of_tyres)
print()

print("About car")
car = Car(4,"x")
print(car.no_of_tyres)
car.display()
car.start()
print(car.no_of_gears)