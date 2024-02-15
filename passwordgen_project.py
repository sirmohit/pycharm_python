import random
print("Welcome to password generator")
a =int(input("enter the digit you want: "))
b= int(input("enter the letters you want : "))
c = int(input("enter the symbols you want : "))
l1 = ['0','1','2','3','4','5','6','7','8','9']
l2 = ['T' ,'H' ,'E' ,'Q' ,'U' ,'I' ,'C' ,'K' ,'B' ,'R' ,'O' ,'W' ,'N' ,'F' ,'O' ,'X' ,'J' ,'U' ,'M' ,'P' ,'S' ,'O' ,'V' ,'E' ,'R' ,'T' ,'H' ,'E' ,'L' ,'A' ,'Z' ,'Y' ,'D' ,'O', 'G' ,'t' ,'h' ,'e' ,'q' ,'u' ,'i' ,'c' ,'k' ,'b' ,'r' ,'o', 'w' ,'n' ,'f', 'o' ,'x' ,'j' ,'u', 'm' ,'p' ,'s', 'o' ,'v' ,'e' ,'r' ,'t' ,'h' ,'e' ,'l' ,'a' ,'z' ,'y' ,'d' ,'o' ,'g']
l3 = ['`','~' ,'!' ,' @' ,' #' , '$', '%' ,'^' ,'&' ,'*' ,'(' ,')' ,'<' ,'>' ,',' ,'.' ,'?' ,'/' ,'|']
'''easy password
password = ""
for i in range(1,a+1):
    cha = random.choice(l1)
    password = password + cha
for i in range(1,b+1):
    n =random.choice(l2)
    password = password+n
for i in range(1,c+1):
    m = random.choice(l3)
    password = password  + m
print(password)'''

#strong password
password_list = []
for i in range(1,a+1):
    cha = random.choice(l1)
    password_list.append(cha)
for i in range(1,b+1):
    n =random.choice(l2)
    password_list.append(n)
for i in range(1,c+1):
    m = random.choice(l3)
    password_list.append(m)
random.shuffle(password_list)
password = ""
for i in password_list:
    password = password + i
print(password)


