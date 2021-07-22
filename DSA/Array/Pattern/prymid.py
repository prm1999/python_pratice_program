# Inverted Pyramid of Numbers
# 666666
# 55555
# 4444
# 333
# 22
# 1

num=int(input())
for i  in range(num+1,0,-1):
    print()
    for j in range(0,i):
        print(i,end="")
