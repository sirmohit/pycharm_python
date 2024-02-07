# What is difference between (iterator,iterable and generator)
#generator :
'''def simple_function(n):
    for i in range(n):
        print(type(n))
        print(i)
simple_function(10)'''

#GENERATIVE FUNCTION
'''def gen(l1):
    for i in l1:
         yield(i) # hare "yied"act as a generator
l1 = [12,23,34,45,23]
print(gen(l1))
for i in gen(l1):# printing the value by generator function
    print(i)'''

#FIBONACCI SERIES
'''def fivo(n):
    fn = 0
    sn = 1
    for i in range(n):
        yield fn
        fn,sn=sn,fn+sn
for i in fivo(10):
    print(i)'''

def fibo1():
    a =0
    b=1
    while True:
        yield a # it will generate the data
        a,b = b,a +b
fib = fibo1()
for i in range(10):
    print(next(fib))

s = "mohit"
for i in s:
    print(i)
print()

#next(s)#it will show string is not an iterator
#now see we make our string itrator then i twill become iterable
s1 = iter(s)
print(type(s1))
print(next(s1))
print(next(s1))
print(next(s1))
print(next(s1))
print(next(s1))
print()

#iter(10) #it will show int object is not iterable

def count_test(n):
    count = 1
    while count<=n:
        yield count
        count =count +1
for i in count_test(10):
    print(i)
