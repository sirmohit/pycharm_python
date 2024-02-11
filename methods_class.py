class Instructor:
    follwer = 0 # class object variable
    def __init__(self,name,add):
        print("Welcome to world of python")
        self.name = name
        self.add =add
        #self.follwer =0
        #function become method when it attach to object
    def display(self,tech):
        print("Hi I am in display method")
        print(f"Hi I am {self.name}")
        print(f"I teach {tech}")
    def update_follower(self):
        self.follower = 1
        print(self.follower)
ins_1 = Instructor("Jenny","Delhi")
print(ins_1.name , ins_1.add, ins_1.follwer)
ins_1.display("java")
ins_2 = Instructor("Mohit","Mumbai")
print(ins_2.name, ins_2.add , ins_2.follwer)
ins_2.update_follower()
