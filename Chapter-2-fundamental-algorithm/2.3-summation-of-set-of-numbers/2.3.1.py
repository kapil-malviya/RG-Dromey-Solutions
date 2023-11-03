'''
Design an algorithm to compute the average of n numbers.

'''
 

def compute_average(numbers):
    if not numbers:
        return 0

    total = 0
    n = len(numbers)

    for num in numbers:
        total += num

    average = total / n
    return average


numbers = [1, 2, 3, 4, 5]

average = compute_average(numbers)

print('Average : ', average)
