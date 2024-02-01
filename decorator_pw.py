'''def deco(func):
    def inner_dec():
        print("this is the start of my function")
        func()
        print("this is the end of my function")
    return inner_dec
@deco#here we call the test function fist it will call the "deco"function and then it take the test function as arg and decorate it and return it ,and we can call this deco function on any function you want
def test1():
    print(12+23)
test1()'''

# Make a decorator method to find the time taken by a function for its execution
import time
def showTime(fun):
    def timer_test_inner():
        start = time.time()
        fun()
        end = time.time()
        print(end - start)
    return timer_test_inner
@showTime# this decorator will show the time toexecute the funcions operation
def add():
    print(12+23)
add()
print()

@showTime
def test():
    for i in range(233453655):
        pass
test()