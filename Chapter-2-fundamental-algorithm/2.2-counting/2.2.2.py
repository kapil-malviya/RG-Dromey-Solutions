'''
Design an algorithm that reads a list of numbers and makes a count of the number of negatives and the number of non-negatives members in the set.

'''

def count(numbers):
    negative_count = 0
    non_negative_count = 0

    for number in numbers:
        if number < 0:
            negative_count += 1
        else:
            non_negative_count += 1

    return negative_count, non_negative_count


numbers = [2, -5, 3, -1, 0, 6, -7]
result = count(numbers)
print(f'Negative numbers : {result[0]}, Non-negative numbers : {result[1]}')

integers = [2, 2]
negatives, non_negatives = count(integers)
print('Number of negative numbers : ', negatives)
print('Number of non-negative numbers : ', non_negatives)