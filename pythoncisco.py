
"""
def f(inp=2,out=3):
    return inp*out
print(f(out=2))

a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)

def f(a,b):
    return b**a
print(f(b=2,2))


z=0
y=10
x=y<z or z>y and y>z or z<y
print(x)


x=3
y=2
x=x%y
x=x%y
y=y%x
print(y)



d={ 'one':'two','three':'one','two':'three'}
v=d['three']
for k in range (len(d)):
    v=d[v]

print(v)





x=float(input())
y=float(input())
print(y**(1/x))


def f(x):
    if x%2==0:
        return 1
    else:
        return 2
print(f(f(2)))


y=(input())
x=(input())
print(x+y)

dd={"1":"0","0":"1"}
for x in dd.vals():
    print(x,end=" ")



x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)


class A:
    pass

class B( A):
    pass
class C (B):
    pass

print(issubclass(A,B))


class A:
    def __init__(self,v):
        self._a=v+1
a=A(0)
print(a._a)






class A:
    
    def a(self):
        
        print('a')

class B:
    def a(self):
        print('b')

class C(A,B):
    def c(self):
        self.a()

o = C()

o.c()





d={1:0,2:0,3:2,0:1}
x=0
for y in range (len(d)):
    x=d[x]

print(x)

dct={}
dct['2']=(1,2)
dct['1']=(3,4)
for x in dct.keys():
    print(dct[x][1],end=" ")



ls=[[ c for c in range (r)]for r in range (3)]
for x in ls:
    if len(x)<2:
        print()


d={ 'one':1,'two':2,'three':3}
for k in sorted (d.values()):
    print(k,end=' ')




str='abcdef'
def f(s):
    del s[2]
    return s
print (f(str))








def a(x):
    def b():
        return x+x
    return b
x=a('x')
y=a('')
print(x()+y())










class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()

a=A()
print(a.g())

"""

class A:
    pass
class B:
    pass

class C(A,B):
    pass
print(issubclass(A,C) )











