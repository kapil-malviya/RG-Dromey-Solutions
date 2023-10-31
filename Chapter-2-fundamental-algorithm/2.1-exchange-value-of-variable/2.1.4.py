'''
Given two vaiables of integer type a and type b, exchange their values without using a third temporary variable.

'''

# Initialize values of a and b
a = 8
b = 28

# exchange values without using temporary variable
'''
a = a + b
b = a - b
a = a - b
'''

a, b = b, a

# Now, the values of a and b have been exchanged
print("a:", a)
print("b:", b)
