'''
Design an algorithm to compute the sum of the squares of n numbers.

''' 

def sum_of_squares(numbers):
    total = 0

    for num in numbers:
        total += num ** 2

    return total


numbers = [1, 2, 3, 4, 5]

result = sum_of_squares(numbers)

print(result)
