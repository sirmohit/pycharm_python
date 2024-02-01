# conditional statement or decision making statement : if,else if , else if ladder ,elif
'''
height = int(input("Enter your height : "))
if(height>3):
    print("ticket is required")
else:
    print("no ticket is required")
'''
print()
'''
# Nested if else & elif
height = int(input("Enter your height : "))
if(height>3):
    print("You can ride")
    age = int(input("Enter Your age : "))
    if(age > 18):
        print("you have to pay 250")
    elif(age<18 and age>10):
        print("You have to pay 100")
    elif(age<10):
        print("You are not eligible to ride")
else:
    print("You age not eligible to take ride")
print("Thanks for visiting")'''
print()
height= int(input("Enter your height : "))

bill =0
if(height>3):
    print("you can ride")
    age = int(input("Enter your age : "))
    if(age<12):
        bill = 150
        print(f"You ticket is of {bill} ")
    elif(age<18):
        bill = 250
        print(f"your ticket is of {bill}")
    else:
        bill=500
        print(f"your ticket is of 500")
    take_photo = input("want to take photo : ")
    if(take_photo == 'y'or take_photo =='Y'):
        bill = bill +50
        total_bill=bill
        print(f"your total bill is {bill}")
else:
    print("you can't take ride")

