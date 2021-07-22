#Seprate positive and negative according to order


arr=[2,-3,5,-4,6,-8]
c=[]
d=[]
for i in range(0,len(arr)):
    if(arr[i]>0):
        c.append(arr[i])
    else:d.append(arr[i])
print(c+d)



