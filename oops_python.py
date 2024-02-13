class Instructor:#sytax of class
    def __init__(self,name,add): #to initialize the data member of a class while creating a object,it always called when creating a object,"self" is refering  actual object used to bind the arribute ot current object.
        print("I am in current object")
        self.name = name
        self.add = add
        self.follower = 0 #default attribute

instructor_1 = Instructor("mohit",'Badnoor')# creation of object
print(type(instructor_1))
print(instructor_1.name)
print(instructor_1.follower)

instructor_2 = Instructor("jenny","weraewrwer")
print(f"My name is {instructor_2.name} I belong to {instructor_2.add}")
#instructor_1.name = "payal" # here name is attribute as it is attach to object instructor
# constructor : it allow us to store the value of the data member of a class we can iniatialize the value to attribute

