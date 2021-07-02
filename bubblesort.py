def bubblesort(arr):
    n = len(arr)
    countc = 0
    for j in range(n - 1):
        for item in range(0, n - j - 1):
            if arr[item] > arr[item + 1]:
                arr[item], arr[item + 1] = arr[item + 1], arr[item]
                countc = countc + 1
    print(countc)
    return arr


arr = [7, 1, 0, 8, 5, 9, 12, 6]
x = bubblesort(arr)
print(x)


# Complexity Worst and Average Case Time Complexity: O(n*n).
# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
# Stable: Yes


# using bool value reduce the complexity
def bubblesortwithbool(arr):
    n = len(arr)
    count = 0
    for i in range(0, n):
        swap = False  # for check if the swap is possible
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                count = count + 1

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if swap == False:
            break
    print(count)

    return arr


arr = [7, 8, 0, 4, 9, 5, 12, 100, 6, 89, 50]
xwith_bool = bubblesortwithbool(arr)
print(xwith_bool)
