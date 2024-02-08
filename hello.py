'''
print("hello")
#Data types
a = 10
print(type(a))
print(id(a))
a = 10.0
print(type(a))
print(id(a))
x = 0o123
print(x)
print(type(x))
y = 0x234
print(y)
print(type(y))
b= "Mohit Bhade"
print(b[3])
print(b[1:7:2])
print(type(b))
c = {1,2,3,4,5,6}
print(type(c))
d = [1,2,3,4,5]
print(type(d))
e = (12,34,45,56)
print(type(e))
f= False
print(type(f))
g = 23+3j
print(type(g))
h = {"hello":"python"}
print(type(h))
print(g.imag)
print(g.real)
a,v,g = 12,34,56
print(a)
print(v)
print(g)
#local variable
def add():
    a= 12
    b= 23
    c = a+b
    print("the sum is ", c)
add()
# STRING MANIPULATION
print("String Manipulation Exercise\nString Concatenation is done with '+' Sign\ne.g.print('Hello' + 'Jenny')\nNew Line can be created with a backslash and n")

# Input Function
#print("Hey" + " "+input("What is your name ?")+",how are you")
'''
# variables in python
'''
name = input("What is your name ?")
length = len(name)
print(length)
'''
'''
#swap two number
a= 1
b= 2
a = a+b
b= a-b
a= a- b
print("a is ",a)
print("b is ",b)

#skip special meaning of string
print("My learning\'s \"starts from here\"")

# type casting
length = len("Mohit Bhade")
print("Length of your name is " + str(length) + " character")
print(int("19")+ int("21"))

first_number = input("Enter your first number : ")
second_number = input("Enter your second number : ")
print(int(first_number) + int(second_number))

a= input("Sum of every number of given digit is : ")
print(int(a[0]) + int(a[1]),"\n")

# Arithmetic Operator +,-,*,**,/,//,%,()
a= 12
b = 32
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b,"\n")

# Assignment Operator +=,-=,*=,/=,//=,**=,%=
a= 12
b = 32
a+= 34
a-=23
a/=456
a//=12
a*=2
a**=5
a%=2
print(a)

print(a)
print(a)
print(a)
print(a)
print(a)
print(a)

# Comparision Operator <,>,<=,>=,==,!= they return always a boolean value
# Logical Operator "and,or,not" which are used to combine conditional statement
# Bitwise Operator :which used to work on binary number (&,|, ^ ,~, <<,>>)
    & if both bits are same it give you 1 otherwise 0
   | if any bits are 1 it give you 1 other wise 0
   ^ if if both bits are same it will give you 0 any of them are differ it give you 1
   ~ negation of any number would be -(number + 1)
   << left shift any number by n the fomula is : (number * n^n)
   >> right shift any number by n the fomula is :(number/2^n)

# Identity Operator (is ,is not) it basically compare the add. of the object and returns the boolean value
v = 5
b = 5
print(v is b)# it will compare the add.of the object 5
print(id(b))
print(id(v))

print(b is not v,"\n")
'''
# Membership Operator ("in" and "not in") : It returns boolean value by checking whether the item present in the sequence or not
s= "Mohit Bhade"
print('M' in s)
print('m' in s)
print(' ' in s)
l= [1,2,3,'d',"wer",12+4j]
print('e' in "wer")
print(1 in l)