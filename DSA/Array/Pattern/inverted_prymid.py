# 54321
# 4321
# 321
# 21
# 1


num = int(input())
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
