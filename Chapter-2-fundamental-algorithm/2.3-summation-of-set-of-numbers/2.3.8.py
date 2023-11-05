'''
Develop an algorithm to compute the sum of the first n terms (n>=1) of the series 
    s = 1-3+5-7+9-...
 
'''


def sum_of_series(n):
    if n < 1:
        return 0

    total = 0
    current_term = 1
    sign = 1               # start with positive sign

    sequence = []           # to store series

    for i in range(n):
        total += current_term * sign
        sequence.append(current_term * sign)
        current_term += 2            # move to next term
        sign = -sign                # toggle sign for next term

    return total, sequence

n = 10

result = sum_of_series(n)

print(result[0])
print(result[1])
