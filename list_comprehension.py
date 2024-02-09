# COMPREHENSION : IT A SHORT HAND WAY TO DO A RETATIVE TASK IN LESS CODE
# SYNTAX : IF I TIS LIST [VARIABLE_TO_STORE_OUTCOME for VARIABLE in LIST_NAME CONDITION IF YOU WANT TO PROVIDE]
# find the square of the items present in the list using loop
l1 = [1,2,3,4,5,6]
l2 = []
for i in l1:
    l2.append(i**2)
print(l2)
print()

#find the square of the items present in the list using list comprehension
l1 = [1,2,3,4,5,6]
print("Squre using list comprehension :",[i**2 for i in l1])

#find the even  items present in the list using list comprehension
l1 = [1,2,3,4,5,6]
print("Even number in the list are :",[i for i in l1 if i%2==0])

#convert the list items in uppercase present in the list using list comprehension
l2 =["mohit","aniket","sourav","deepak"]
print("uppercase list is :",[i.upper() for i in l2])

#dictionary comprehension
# find the square of the value of the dictionary
d= {"key1":1,"key2": 2,"key3":3,"key5":5}
print({k:v**2 for k,v in d.items()})

# find the  value of the greater than 1 dictionary
d= {"key1":1,"key2": 2,"key3":3,"key5":5}
print({k:v for k,v in d.items() if v>1})
