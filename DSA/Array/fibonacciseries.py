# Fibonacci Series


def fibonacci_series(num):
    if num == 0:
        return 1
    elif (num == 1):
        return 1
    elif (num > 1):
        return fibonacci_series(num - 1) + fibonacci_series(num - 2)


num = int(input())
for i in range(0, num):
    p = fibonacci_series(i)
    print(p)
