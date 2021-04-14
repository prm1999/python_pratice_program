#pallidrom of number and string



x=int(input())
rev=0
temp=x
while(x>0):
    rem=x%10
    rev=rem+rev*10
    x=x//10
print(rev)
if(temp==rev):
    print(True)
else:print (False)


