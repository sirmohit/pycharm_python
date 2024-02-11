# map():it map the values given to it according to the function written in it
# finding the square of list
'''l1 = [1,2,3,4,5,6]
def sq(x):
    return x**2
print(list(map(sq,l1)))
print()

#now see
print(list(map(lambda x: x**2,l1)),"\n")

l =[1,2,3,4,5,6,7,8]
l2=[12,23,34,45,56,67,78,89]
print(list(map(lambda x,y:x+y,l,l2)),'\n')

s = "pwskills"
print(list(map(lambda s:s.upper(),s)))'''

#REDUCE FUNTION :it colapse the value
'''from functools import reduce
l = [1,2,3,4,4,5]
print(reduce(lambda x,y:x+y,l))
print(reduce)

print(reduce(lambda x,y:x*y,l),'\n')

print(reduce(lambda x,y:x if x>y else y,l),'\n')'''

#filter function
l = [12,23,43,234,54]
print(list(filter(lambda x:x%2 ==0,l)),'\n')

print(list(filter(lambda x:x%2 !=0,l)),'\n')

l1 = [-1,-476,12,86]
print(list(filter(lambda x:x<0,l1)),'\n')

s = ["mohit","pwskills","banglore","sudh","krish"]
print(list(filter(lambda x:len(x)<6,s)))
