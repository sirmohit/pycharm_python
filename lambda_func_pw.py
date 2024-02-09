'''def test(n,p):
    return(n**p)
print(test(2,3))
print()'''

#lamda function or annonmus function
print(lambda n,p:n**p)
a = lambda n,p :n**p # here it take n and p as input and perform the given operation and return the value
print(a(2,3),'\n')

add = lambda a,b: a+b
print(add(12,23))

mul = lambda a,b:a*b
print(mul(2,3))

# write a program to convert celceius to ferhenheight
c_to_f = lambda c : (9/5)*c +32
print(c_to_f(37))

# find max number
finding_max = lambda x,y:x if x>y else y
print(finding_max(12,32))

find_length = lambda a :len(a)
print(find_length("adfadf"))