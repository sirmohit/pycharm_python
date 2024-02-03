try:
    f = open("text",'r')
except Exception as e:
    print("this is my except block",e)
print(23+3,"\n")

try:
    f= open("text",'w')
    f.write("write into my file")
    f.close()
except Exception as e:
    print("this is my except block",e)
print()

try:
    f= open("text",'w')
    f.write("write into my file")
except Exception as e:
    print("this is my except block",e)
else:
    f.close()
    print("this will be executed if you execute without error")
print()

try:
    f= open("text1",'r')
    f.write("write into my file")
except Exception as e:
    print("this is my except block",e)
else:
    f.close()
    print("this will be executed if you execute without error")

try:
    f= open("text2",'r')
    f.write("write into my file")
finally:
    print('finally will execute at any condtion')
'''except Exception as e:
    print("this is my except block",e)
else:
    f.close()
    print("this will be executed if you execute without error")'''
