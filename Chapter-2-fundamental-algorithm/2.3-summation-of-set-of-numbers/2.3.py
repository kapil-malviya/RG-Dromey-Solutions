'''
Given a set of n numbers design an algorithm that adds these numbers and return the resultant sum. Assume n is greater than or equal to zero.

'''


def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add_numbers([1, 2, 3, 4, 5])
print('Sum of numbers : ',result)