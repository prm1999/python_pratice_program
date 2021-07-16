# find Largest sum contiguous Subarray [V. IMP]
def kanadeAlgo(A):
    max_so_far = A[0]  # initalize maximum value
    max_end_here = A[0]  # maxmium at sublist ending at current postion
    for i in range(1, len(A)):
        max_end_here = max_end_here + A[i]
        max_end_here = max(max_end_here, A[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far


A = [-1, -2, -3, -4]
print("K", kanadeAlgo(A))


def kanadeAlgoSum(AB):
    max_so_far = 0 # initalize maximum value
    max_end_here = 0# maxmium at sublist ending at current postion
    start = end = 0
    beg = 0
    for i in range(len(AB)):
        max_end_here = max_end_here + AB[i]

        if max_end_here < 0:
            max_end_here = 0
            beg = i + 1
        if max_so_far < max_end_here:
            max_so_far = max_end_here
            start = beg
            end = i
    print(max_so_far)
    print(AB[start:end + 1])


AB = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
kanadeAlgoSum(AB)

#
#


# Function to print contiguous sublist with the largest sum
# in a given set of integers
def kadane(A):
    # stores maximum sum sublist found so far
    maxSoFar = 0

    # stores the maximum sum of sublist ending at the current position
    maxEndingHere = 0

    # stores endpoints of maximum sum sublist found so far
    start = end = 0

    # stores starting index of a positive-sum sequence
    beg = 0

    # traverse the given list
    for i in range(len(A)):

        # update the maximum sum of sublist "ending" at index `i`
        maxEndingHere = maxEndingHere + A[i]

        # if the maximum sum is negative, set it to 0
        if maxEndingHere < 0:
            maxEndingHere = 0  # empty sublist
            beg = i + 1

        # update result if the current sublist sum is found to be greater
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i

    print("The sum of contiguous sublist with the largest sum is", maxSoFar)
    print("The contiguous sublist with the largest sum is", A[start: end + 1])


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
kadane(A)
