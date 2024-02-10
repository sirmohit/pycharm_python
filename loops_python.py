# for loop : for loop is more likely to be an iterator to iterate over a sequence of items.
# syntax : for variable_name in sequence_item_container_name:
list2 = [23,34,45,54,"mohit",23.43]
for item in list2:
    print(item)
print()

s = "Mohit Bhade"
for m in s:
    print(m)
print()

sq = []
list23 = [12,23,34,45,45]
for i in list23:
    square = i**2
    sq.append(square)
print(f"List of squares is : {sq}")
print()

# FOR_ELSE : THE ELSE PART OF FOR_ELSE IS EXECUTED ONLY WHEN THE FOR LOOP IS SUCCESSFULLY COMPLETED
print("FOR_ELSE")
tupl1 = (1,2,3,4,5,54)
for i in tupl1:
    print(i)
else:
    print("for loop is successfully completed")

for j in tupl1:
    print(j)
    if j == 5:
        break
else:
    print("problem in loop")
print()

#WRITE A PROGRAM TO FIND THE AVERAGE OF LIST
'''
height = input("Enter your heights: ")
#split the height
height_list = height.split()
count = 0
#taking the length of lisst
for i in height_list:
    count = count + 1
print(count)
# converting the list into int
total = 0
for i in range(count):
    height_list[i]= int(height_list[i])
    total = total + height_list[i]
avg = total / count
print(round(avg))'''
print()

# WAP TO FIND THE MAX ELEMENT OF LIST
#creating a empty list
# creating an empty list
'''
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
	i = int(input())
	# adding the element
	lst.append(i)
print(lst)
maxl = 0
for i in lst:
    if(i>maxl):
        maxl = i
print(f"max element in the list is {maxl}")'''
print()

# WAP TO FIND THE MINIUM ELEMENT OF THE LIST
'''
l = []
n = int(input("Enter the size of list : "))
for i in range(0,n):
    i = int(input())
    l.append(i)
print(l)
min = l[0]
for i in l:
    if i <min:
        min = i
print(min)'''




