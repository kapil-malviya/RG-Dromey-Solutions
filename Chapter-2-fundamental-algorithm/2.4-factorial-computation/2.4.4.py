'''
Design an algorithm which, given some integer n, finds the largest factorial number present as a factor in n
  
'''

def largest_factor(n):
    factorial = 1
    i = 1
    largest_factorial = 1
    while factorial <= n:
        if n % factorial == 0:
            largest_factorial = factorial
        i += 1
        factorial *= i
    return largest_factorial

n = 788
largest_factorial = largest_factor(n)
print(f'The largest factorial factor of {n} is {largest_factorial}')
