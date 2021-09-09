"""


i=0
while i<5:
    i+=1
    if(i%2==0):
        break
    print("*")


my=[1,2,3]
for v in range(len(my)):
    my.insert(1,my[v])
print(my)

i=0
while i<=3:
    i+=2
    print("*")


myl=[3,1,-2]
print(myl[myl[-1]])


myli=[[0,1,2,3] for i in range(2)]
print(myli[2][0])


x=1
print(x==x==x)


var=1
while var<10:
    print("*")
    var=var<<1


vals=[0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)



nums=[1,2,3]
vals=nums[-1:-2]
print(vals)


mylist=[ i for i in range(-1,2)]
print(mylist)



var=0
while var<6:
    var+=1
    if var %2==0:
        continue
    print("g")



mylist=[1,2,3]
mylist1=[]
for v in mylist:
    mylist1.insert(0,v)
print(mylist1)


t=[[3-i for i in range(3)] for j in range (3)]
s=0
for i  in range(3):
    s+=t[i][i]
print(s)

a=1
b=0
c=a&b
d=a|b
e=a^b

print(c+d+e)




for i in range(1):
    print("h")
else:
    print("g")



mylist=[1,2,3,4]
print(mylist[-3:-2])


tup=(1,2,4,8)
tup=tup[1:-1]
tup=tup[0]
print(tup)



def fun(x):
    global y
    y=x*x
    return y
fun(2)
print(y)


def fun(x):
    x+=1
    return x
x=2
x=fun(x+1)
print(x)







def f(x,y,x):
    return x+2*y+2*z

print(f(0,z=1,y=3))


def fun(x):
    if(x%2==0):
        return 1
    else:
        return

print(fun(fun(2))+1)

def fun(a):
    return a**a

def fun1(a):
    return fun(a)*fun(a)

print(fun1(2))



def any():
    print(var+1,end="")

var=1
any()
print(var)








m=[1,2]
for v in range(2):
    m.insert(-1,m[v])

print(m)

d={"1","0","0","1"}
for x in d.vals():
    print(x,end="")


i=0
while i<i+2:
    i+=1
    print("*")
else:
    print("*")


lis=[i for i in range(-1,-2)]
print(lis)

print("a","b","c",sep="sep")


z=0
y=10
x=y<z and z>y or y>z and z<y
print(x)



t=[[x for x in range(3)] for j in range (3)]

for r in range(3):
    for c in range(3):
        if t[r][c]%2!=0:
            print("#")


ml=[x*x for x in range(5)]
def fun(lis):
    del lis[lis[2]]
    return lis

print(fun(ml))


di={}
di['1']=(1,2)
di['2']=(2,1)
for x in di.keys():
    print(di[x][1],end="")



def fun(a,b):
    return b**a

print(fun(b=2,2))

x=1//5+1/5
print(x)


nums=[1,2,3]
vals=nums
del vals[:]
print(vals)


def fun(inp=2,out=3):
    return inp*out

print(fun(out=2))



def fun(x):
    if x%2==0:
        return 1
    else:
        return 2

print(fun(fun(2)))



def fun(a):
    return None

def fun1(a):
    return fun(a)*fun(a)

print(fun1(2))


def fun(x,y):
    if(x==y):
        return x
    else:
        return fun(x,y-1)
print(fun(0,3))




tup=(1,2,4,8)
tup=tup[-2:-1]
tup=tup[-1]
print(tup)



a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)




x=int(input())
y=int(input())
x=x%y
x=x%y
y=y%x
print(y)


x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)




x=float(input())
y=float(input())

print(y**(1/x))





import math
result=math.e!=math.pow(2,4)
print(int(result))


from random import randint

for i in range(2):
    print(randint(1,2),end="")




print(ord('c')-ord('a'))
print("Mike">"Mikey")


print(chr(ord("z")-2))


try:
    print("5"/0)
expect ArithmeticError:
    print("arith")
expect ZeroDivisionError:
    print("zero")
expect:
    print("some")


x='\''
print(len(x))

print(3*'abc'+'xyz')

def o(p):
    def q():
        return "*"*p
    return q
r=o(1)
s=o(2)
print(r()+s())

b=bytearray(3)
print(b)



def f(n):
    s='+'
    for i in range(n):
        s+=s
        yield s
for x in f(2):
    print(x,end="")

import os
os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes=['small','medium','large']

for size in sizes:
    os.mkdir(size)
print(os.listdir())



import calendar
print(calendar.weekheader(2))

from datetime import date
date1=date(1992,1,16)
date2=date(1991,2,5)
print(date1-date2)

import os
os.mkdir('pictures')
os.chdir('pictures')
#os.mkdir('thumbnails')
#os.chdir('thumbnails')
#os.mkdir('tmp')
#os.chdir('../')
print(os.getcwd())


import math
print(dir(math))


class A:
    pass

class B( A):
    pass
class C (B):
    pass

print(issubclass(A,C))

print(chr(ord("p")+2))
x='\\\'
print(len(x))

import os
os.mkdir('pictures/thumbklins')
os.rmdir('pictures')


class A:
    def __init__(self,name):
        self.name=name
a=A("class")
print(a)


def fun(x):
    return 1 if x%2!=0 else 2
print(fun(fun(1))



print(len([i for i in range(0,-2)]))

t=(1,)
t=t[0]+t[0]
print(t)

z=2
y=1
x=y<z and z>y or y>z and z<y
print(x)


x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)



print(len((1,)))
"""

def a(x):
    def b():
        return x+x
    return b
x=a('x')
y=a('')
print(x()+y())


d={}
d['2']=[1,2]
d['1']=[3,4]
for x in d.keys():
    print(d[x][1],end="")


i=4
while i>0:
    i-=2
    print("*")
    if i==2:
        break
else:
    print("*")





































































    














































































