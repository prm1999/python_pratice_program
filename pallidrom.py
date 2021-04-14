n=int(input())
num=0
while(n>0):
    rem=n%10
    n=n//10
    num=rem+num*10
    print(rem)
print(num)
if(n==num):print("Pallidrome")
else:print("Not Pallidrom")
