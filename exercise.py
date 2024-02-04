# Calculate the bmi of a person
'''
a= int(input("Enter your weight : " "\n"))
b= float(input("Enter your height : " "\n"))
c= a//b**2
print("your bmi is : ",int(c))
'''
'''
a= int(input("Enter your weight : " "\n"))
b= float(input("Enter your height : " "\n"))
c= a//b**2
print("your bmi is : ",int(c))
if(c<18):
    print(f"Your bmi is {c} and you age under weight")
elif(c<25):
    print(f"Your bmi is {c} and you are normal weight")
elif(c<30):
    print(f"Your bmi is {c} and you are overweight")
elif(c<35):
    print(f"Your bmi is {c} and you are obese")
else:
    print(f"your bmi is {c} and you are clinically obese")'''
print()
# check whether the year is leap year or not
# if the year is divisible by 4,100and 400 it leap year otherwise not
'''
year = int(input("Enter the year : "))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("It is a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap year")
else:
    print("It's not a leap year")'''

'''
# WAP for the pizza bill receipt
size = input("Enter the size of pizza :")
bill = 0
if(size == 's'or size == 'S'):
    bill = 100
    print(f"your bill is {bill}")
elif(size == 'm'or size=='M'):
    bill = 200
    print(f"your bill is{bill}")
else:
    bill = 300
    print(f"your bill is {bill}")
want_pepperoni = input("Want peproni ")
if(want_pepperoni == "y"or want_pepperoni == 'Y'):
    if (size == 's' or size == 'S'):
        bill = bill+30
    else:
        bill = bill+50
want_excheese = input("want cheese")
if(want_excheese == 'y'):
        bill = bill+20
print(f"Your total bill is {bill}")
print("Thanks for visiting")'''

'''
# WAP a program to calculate love calculator
name1 = input("Enter your name : ")
name2  = input("Enter your name : ")
final_name = name1 + name2
final_name=final_name.lower();
t= final_name.count('t')
r= final_name.count('r')
u= final_name.count('u')
e= final_name.count('e')
true = t+r+u+e
l= final_name.count('l')
o= final_name.count('o')
v= final_name.count('v')
e= final_name.count('e')
love = l+o+v+e
love_score = str(true)+str(love)
print(f"Your love percent is : {love_score} %")'''



