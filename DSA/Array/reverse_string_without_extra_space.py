str1="Anurag"
str=list(str1)
p=len(str)
mid=p//2
i=0
j=p-1
while(i<j):
    str[i],str[j]=str[j],str[i]
    i+=1
    j-=1
print("".join(str))