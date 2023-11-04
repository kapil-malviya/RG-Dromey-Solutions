'''
Develop an algorithm to compute the sums for the first n terms (n>=0) of the following series:
a)  s = 1+2+3+...
b)  s = 1+3+5+...
c)  s = 2+4+6+...
d)  s = 1+1/2+1/3+...

''' 

# series a sum

def sum_a(n):
    if n < 0:
        return 0 

    total = 0

    for i in range(1, n + 1):
        total += i
    
    return total



# series b sum

def sum_b(n):
    if n < 0:
        return 0

    total = 0
    term = 1

    for i in range(n):
        total += term
        term += 2

    return total


# series c sum

def sum_c(n):
    if n < 0:
        return 0

    total = 0
    term = 2

    for i in range(n):
        total += term
        term += 2

    return total

# series d sum

def sum_d(n):
    if n < 0:
        return 0

    total = 0

    for i in range(1, n + 1):
        total += 1/i
 
    return total


n = 8

result_a = sum_a(n)
result_b = sum_b(n)
result_c = sum_c(n)
result_d = sum_d(n)

print('Sum of series a) : ', result_a)
print('Sum of series b) : ', result_b)
print('Sum of series c) : ', result_c)
print('Sum of series d) : ', result_d)
