# A basic code for matrix input from user

R = int(input())
N=int(input())
# Initialize matrix

matrix = []
count=0
# For user input
for k in range(N):
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(R):  # A for loop for column entries
            a.append(int(input()))
            if ((a[i][j] == "A" and a[i + 1][j + 1] == "B") or (a[i][j] == "B" and a[i + 1][j + 1] == "C") or (
                    a[i][j] == "C" and a[i + 1][j + 1] == "A")):
                count=count+1

        matrix.append(a)
print(count)
"""# For printing the matrix
for i in range(R):
    for j in range(R):
        print(matrix[i][j], end=" ")
    print()
"""
