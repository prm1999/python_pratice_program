# factorial Program


num = int(input())
fac = 1
i = 1
for i in range(1, num + 1):
    fac = fac * i
print(fac)


# By recursive method
def factoral(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factoral(num - 1)


num = int(input())
print(factoral(num))
