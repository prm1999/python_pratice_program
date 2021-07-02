print("hello")
number=int(input("Number:"))
lst=[]

for item in range(number):
    p=int(input())
    lst.append(p)
x=set(lst)
setlist=list(x)
print(setlist)
for i in range (len(x)):
     for j in range(len(lst)):
         
        if(setlist[i]==lst[j]):
        
            print ("yes")
        else: print( "no")
    
print(set(lst))
print(list(lst))
