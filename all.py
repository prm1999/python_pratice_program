"""

#byte array can be manuliplated and array cannot be manuplated
element=[10,20,30,40]
x=bytearray(element)
print(x[2])


# area of circle
radius=float(input("radius:"))
PI=3.14
area=PI*radius*radius
x=float(area)
print("%.2f"%area)
print(round(area,2))# verified menthod

#Range range start from 0 :::in keyword are used
#Print from 0 to 10
for i in range(10):
    print(i)


for i in range (10 ,30,2):  # range( starting point,ending point ,gap in between)
    print(i)
#list is created using the range
lst=list(range(10))      # list will automatically take the value from the 0 to range last value
print(lst)


#sets are used for removing the duplicate value from the sets
ch=set("hello")
print(ch)

ch.update("my")  #update value can add the element the sets
print("After Added Up or Updated",ch)

ch.remove("h")
print("After Removed",ch)

#frozenset datatype
#In the frozen datatype the element cannot be updated or removed from the set

p=frozenset(ch)
ch.remove("m")
print(ch)

"""
#Mapping in the python
d={
