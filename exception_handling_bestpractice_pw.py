#use always a specific error
try:
    a = 10/0
    print(a)
except Exception as e:# not good practice
    print(e)
print()

try:
    a=89/0
    print(a)
except ZeroDivisionError as e:
    print(e)
print()

#print always a proper message
try:
    a=89/0
    print(a)
except ZeroDivisionError as e:
    print("I am trying to handle division by zero error",e)
print()

#always try to log your error
import logging
logging.basicConfig(filename="error.log",level=logging.ERROR)
try:
    a=89/0
    print(a)
except ZeroDivisionError as e:
    logging.ERROR("I am trying to hadle zerodivision error {}".format(e))

#always avoid multiple exception handling
try:
    a=89/0
    print(a)
except FileNotFoundError as e:
    logging.ERROR("iam handling file not found error".format(e))
except AttributeError as e:
    logging.ERROR("iam handling attribute error".format(e))
except ZeroDivisionError as e:
    logging.ERROR("I am handling zero division error".format(e))
except ZeroDivisionError as e:
    print(e)

#document all error
#cleanup all the resources
try:
    with open("test.txt",'w') as f:
        f.write("this is my data to file")
except FileNotFoundError as e:
    logging.ERROR("iam trying to handlr error".format(e))
finally:
    f.close()