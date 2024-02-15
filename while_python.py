# syntax : while condition/expression:
#                 statement to be execute untill the conditionis true
# print digit  1 to 10
'''count = 1
while count<11:
    print(count)
    count = count +1
print()

# while with "else " block
# else will be executed only after the completion of while loop normally but not forcefully by using break, continue,pass keywords
coutn = 1
while(coutn < 20):
    print(coutn)
    coutn +=2
else:
    print("Thanks for your time")
print()

coutn = 1
while(coutn < 20):
    print(coutn)
    coutn +=2
    if coutn == 15:
        break
else:
    print("Thanks for your time")
print()'''

# pw - while loop
'''n= int(input("enter your number : "))
starting_point = 0
counter =1
while(counter <= n):
    starting_point = starting_point + n
    n=n-1
print(starting_point)'''

#factorial of a number
'''a= int(input("Enter a number greater than 0 : "))
if a==1:
    print(a)
else:
    fact = 1
    while(a>=1):
        fact = fact*a
        a=a-1
print(fact)'''

#fibonacci series
'''a = int(input("Enter a number : "))
fn = 0
sn = 1
count = 1
while(count<=a):
    print(fn)
    temp =sn +fn
    fn = sn
    sn = temp
    count =count + 1
print(sn)'''

#revrse a string
'''word = input("Enter a string : ")
reverse = ''
length = len(word)
while(length>0):
    reverse = reverse + word[length-1]
    length=length-1
print(reverse)'''

#table of number
n = int(input("Enter a number whose table you want to print : "))
a = 1
while(a<=10):
    result = a*n
    print(f"{a} * {n} = {result}")
    a=a+1

