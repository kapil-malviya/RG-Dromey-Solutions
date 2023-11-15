'''
Desgn an algorithm to find the sum of the first n terms of the series 

    f = 0! + 1! + 2! + 3! + ...... + n!         (n>=0)


'''


# calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# find sum of the series
def series_sum(n):
    sum_result = 0
    for i in range(n + 1):
        sum_result += factorial(i)
    return sum_result

n = 8
result = series_sum(n)
print(f"sum of first {n} terms is: {result}")