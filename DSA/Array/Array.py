# Write a program to reverse an array or string
# arr=int(input())
def reversearray(arr, start, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)


arr = [1, 7, 8, 9, 4]
reversearray(arr, 0, 4)


#
# # Another approach  print( A[::-1])
# # Maximum and minimum of an array using minimum number of comparisons
#
def maxval(arr, start, end, ):
    max = 0
    min = 0
    for item in range(0, len(arr)):
        if (arr[item] > max):
            max = arr[item]
        else:
            pass
    # while(arr[i]):
    #     if(arr[i]>arr[i+1]):
    #         maxvalue=arr[i]
    #     else:maxvalue=arr[i+1]
    print(max)


def minval(arr, start, end, ):
    min = arr[0]
    count = 0
    for item in range(0, len(arr)):
        if (arr[item] < min):

            min = arr[item]
        else:
            pass
        count = count + 1
    print(min, count)


arr = [7, 8, 9, 4, 12, 4]
minval(arr, 0, 5)


class Solution:
    def kthSmallest(self, arr, l, r, k):
        arr.sort()
        return arr[k - 1]
        return maxval


#
# # Move all the negative elements to one side of the array
#
# # Using two pointer approach
# # Check If the left and right pointer elements are negative then simply increment the left pointer.
# # Otherwise, if the left element is positive and the right element is negative then simply swap the elements, and simultaneously increment and decrement the left and right pointers.
# # Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
# # Repeat the above 3 steps until the left pointer ≤ right pointer.
#
def negative_item_side(arr, left, right):
    while (left <= right):
        if (arr[left] < 0 and arr[right] < 0):
            left += 1
        elif (arr[left] > 0 and arr[right] < 0):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left += 1
        right -= 1


def displayarr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


arr = [-14, 7, -5, -1, 0, 8, -15, 47]
n = len(arr)
negative_item_side(arr, 0, n - 1)
displayarr(arr)


# Union and Intersection of Array

# Function to return the count of number of elements in union of two arrays.

class Solution:
    def doUnion(self, a, n, b, m):
        self.newarr = []
        for k in a:
            self.newarr.append(k)
        for l in b:
            if l not in self.newarr:
                self.append(l)
        return len(self.newarr)


a = [1, 5, 8, 6, 12]
b = [8, 1, 9, 0, 2]
n = len(a)
m = len(b)
Solution()


# find Largest sum contiguous Subarray [V. IMP]
def kanadeAlgo(A):
    max_so_far=A[0] # initalize maximum value
    max_end_here=A[0]# maxmium at sublist ending at current postion
    for i in range(1,len(A)):
        max_end_here=max_end_here+A[i]
        max_end_here=max(max_end_here,A[i])
        max_so_far=max(max_so_far,max_end_here)
    return max_so_far

A=[-1,-2,-3,-4]
print("K",kanadeAlgo(A))





