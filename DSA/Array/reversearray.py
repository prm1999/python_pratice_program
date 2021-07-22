# Reverse the array without reverse functions
a = [1, 2, 8, 0, 15, 1, 2, 9, 10]
c = []
n = len(a)
i = 0
while (n > i):
    temp = a[n - 1]

    c.append(temp)
    n = n - 1
print(c)


# Method 2

def reverse(arr):
    n = len(arr)
    c = []
    for i in range(n - 1, 0, -1):
        temp = arr[i]
        c.append(temp)
    c.append(arr[0])
    print(c)


arr = [1, 2, 8, 0, 15, 1, 2, 9, 10]
reverse(arr)
