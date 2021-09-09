#Half Pyramid Pattern of Numbers

# 1
# 12
# 123
# 1234
# 12345
# 123456





num=int(input())
for i in range(0,num+1):
    n=1
    print()
    for j in range(0,i+1):
        print(n,end="")
        n+=1