"""
stoop="HoolaHoop"
col=stoop.strip("Ho")
print(col)

a=[1,2,3,4,5]
b=lambda x:x[0]+b(x[1:0]) if len(x)>0 else 0
print(b(a))

"""
int num =12
def fun(num):
    if num<=1:
        pass
    elif num%1==1:
        return fun(num-1)
    else:
        return num+fun(num-3)
print(fun(8),num)
