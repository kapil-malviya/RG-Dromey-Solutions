'''
Redesign the algorithm so that it only needs to perform n-1 additions to sum n numbers.

'''
 

def add(numbers):
    if not numbers:
        return 0

    total = numbers[0]        # initialize total with first number
    n = len(numbers)

    for num in numbers[1:]:
        total += num          # perform (n-1) additions

    return total 

result = add([1, 2, 3, 4, 5])
print(result)
