age = int(input("Enter your age : "))
class validateage(Exception):
    def __init__(self,msg):
        self.msg = msg
def validatege(age):
    if age<0:
        raise validateage("Enter age is negative")
    elif age>150:
        raise validateage("Enter age is very high")
    else:
        print("age is valid")
try:
    age = int(input("Enter your age : "))
    validatege(age)
except validateage as e:
    print(e)