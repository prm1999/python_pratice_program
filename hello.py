"""

x=3
y=2
x=x%y
x=x%y
y=y%x
print(y)

x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)

dct={}
dct['1']=(1,2)
dct['2']=(2,1)
for x in dct.keys():
    print(dct[x][1],end=" ")
print("ghgjk")

nums=[1,2,3]
vals=nums
del vals[:]
print(vals)
lst=[i for i in range (-1,-2)]
print(lst)


a=1
b=0
a=a^b
b=a^b
a=a^b

print(a,b)


print("a","b",sep="sep")



x=float(input())
y=float(input())
print(y**(1/x))


dd={"1":"0","0":"1"}
for x in dd.vals():
    print(x,end=" ")





def fun(n):
    s='+'
    for i in range(n):
        s+=s
        yield s
for x in fun(2):
    print(x,end='')





def o(p):
    def q():
        return '*' *p
    return q
r=o(1)
s=o(2)
print(r()+s())


class A:
    A=1
    def __init__(self):
        pass

print(hasattr(A,'a'))


x="\\\\"
print(len(x))


print(chr(ord('p')+2))


import math
print(dir(math))



try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))



print(float("1.3"))



x="\\"
print(len(x))



class A:
    A=1
    def __init__(self):
        self.a=0

print(hasattr(A,'a'))


i=4
while i>0:
    i-=2
    print("*")
    if i==2:
        break
    else:
            print("*")

class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()

a=A()
print(a.g())

ls=[[ c for c in range (r)]for r in range (3)]
for x in ls:
    if len(x)<2:
        print()



        
t=(1,)
t=t[0]+t[0]
print(t)



def a(x):
    def b():
        return x+x
    return b
x=a('x')
y=a('')
print(x()+y())






class A:
    def a(self):
        print(‘a’)

   class B:

      def a(self):

         print(‘b’)

   class C(A,B):

      def c(self):

         self.a()

   o = C()

   o.c()

 





d={ 'one':1,'two':2,'three':3}
for k in sorted (d.values()):
    print(k,end=' ')


class A:
    def __init__(self,v):
        self._a=v+1

a=A(0)
print(a._a)






str='abcdef'
def f(s):
    del s[2]
    return s
print (f(str))


x="""
"""

print(len(x))

print(len((1,)))


v=1+1//2+1/2+2
print(v)

print(len([i for i in range (0,-2)]))


dct={}
dct['2']=(1,2)
dct['1']=(3,4)
for x in dct.keys():
    print(dct[x][1],end=" ")








class A:
    def __init__(self,name):
        self.name=name

a=A("class")


y=input()
x=input()
print(x+y)


x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)



d={1:0,2:0,3:2,0:1}
x=0
for y in range (len(d)):
    x=d[x]

print(x)





def o(p):
    def q():
        return '*'*p
    return q
r=o(1)
s=o(2)
print(r()+s())




y=input()
x=input()
print(x+y)



x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)




x="""
"""

print(len(x))




def f(d,k,v):
    d[k]=v
dc={}
print(f(dc,'1','v'))


def fun(n):
    s=' '
    for i in range(n):
        s+='*'
        yield s
for x in fun(3):
    print(x,end='')



z=2
y=1
x=y<z or z>y and y>z or z<y
print(x)


class A:
    A=1
    def __init__(self):
        self.a=0

print(hasattr(A,'A'))


def f(x):
    return 1 if x %2!=0 else 2
print(f(f(1)))


print(len((1,)))


lt=[1,2,3,4]
lt=list(map(lambda x:2*x,1))
print(lt)




"""

x=16
while x>0:
    print('*',end='')
    x//=2


a= True
b=False
a= a or b
b= a and b
a= a or b
print(a,b)


print(len([i for i in range(0,-2)]))



t=(1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)

