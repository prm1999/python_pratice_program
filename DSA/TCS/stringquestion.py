"""
The function accepts a string „str‟ of length „n‟, that contains alphabets and hyphens (-). 
Implement the function to move all hyphens (-) in the string to the front of the given string. 
Note: Return null if str is null.
"""
string=input()
p=list(string)
count=0
s=[]
for i in range(0,len(p)):
    if(p[i]=='-'):
        p[i].replace('-','888')
        count+=1
    else:s.append(p[i])
        
print(s)
pm=''
print("-"*count+pm.join(s))
