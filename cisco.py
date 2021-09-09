"""vals=[0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

my_list=[1,2,3]
mylist=[]
for v in my_list:
    mylist.insert(0,v)
print(mylist)


x=16
while x>0:
    print("*",end="")
    x//=2


s="abcdef"

def fun(s):
    del s[2]
    return s
print(fun(s))
"""
"""
def check_palindrome(inp_str):
  n=len(inp_str)
  for i in range(n):
    p=inp_str[i]

    x="".join(reversed(p))
    print(x==p)
   
    #for j in x[-1:0]:
        #print(x)
"""
def check_palindrome(inp_str):
  n=len(inp_str)
  for i in range(n):
    p=inp_str[i]
    p_l=p.lower()
    x="".join(reversed(p_l))
    if(x==p_l):
      print(p)
    else :pass
              
              



n=3
p=["hello","Malayalam","Radar"]
p_n=len(p)
check_palindrome(p)
