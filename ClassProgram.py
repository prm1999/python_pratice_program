"""
# Every thing is object in Python
class A:
    for x in range(3):#(0, 1, 2)
        pass
    def __init__(self):#constructor
        pass
a=A()
print(a.x)
        
#Ans 2

class fruit:
    def __init__(self,price):
        self.price=price
obj=fruit(50)

obj.quantity=14
obj.bags=2
print(obj.quantity+len(obj.__dict__))
# dictinary is length =3
#Ans=17
"""

