try:
    a= 23/0
except ZeroDivisionError as e:
    print(e)
print()

try:
    a = int('afdfa')
except (ValueError,TypeError) as e:
    print(e)
print()

#if you don't know the class of exception
try:
    int("adf")
except:
    print("this will catch an error")

#import error
try:
    import sudh
except ImportError as e:
    print(e)
print()

#
try:
    d = {"key":"adf",1:{12,23,34}}
    print(d["key2"])
except KeyError as e:
    print(e)
print()

#
try:
    "sudh".test()
except AttributeError as e:
    print(e)
print()

try:
    l = [1,2,3,4,4]
    print(l[5])
except IndexError as a:
    print(a)
print()

try:
    a = 2 + "adf"
    print(a)
except TypeError as e:
    print(e)
print()

try:
    with open("text.txt",'r') as f:
        test = f.read()
except FileNotFoundError as e:
    print(e)
print()

try:
    with open("text.txt",'r') as f:
        test = f.read()
except Exception as e:# bad practice to call generic class before child class
    print(e)
except FileNotFoundError as e:
    print("text",e)
print()

def test(file):
    try:
        with open("text.txt", 'r') as f:
            test = f.read()
    except Exception as e:  # bad practice to call generic class before child class
        print(e)
    except FileNotFoundError as e:
        print("text", e)
    print()


dir(Exception)