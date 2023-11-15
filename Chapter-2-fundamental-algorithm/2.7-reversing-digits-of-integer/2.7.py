'''
Design an algorithm that accepts a positive integer and reverses the order of its digits.
 
'''


def reverse_digits(n):
    reversedd = 0

    while n > 0:
        digit = n % 10
        reversedd = reversedd * 10 + digit     # append digit to reversed number
        n //= 10                               # remove last digit

    return reversedd

number = 12345
reversed_number = reverse_digits(number)

print(f"original number: {number}")
print(f"reversed number: {reversed_number}")
