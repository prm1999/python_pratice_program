str=input()
lst=list(str)
p=len(lst)

for i in range(0,len(lst)//2):
    lst[i],lst[p-1]=lst[p-1],lst[i]
    i+=1
    p-=1
print("".join(lst))
