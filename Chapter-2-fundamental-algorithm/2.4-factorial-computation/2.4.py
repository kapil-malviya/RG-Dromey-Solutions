'''
Given a number n, compute n factorial (written as n!) where n>=0.
  
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 5
result = factorial(n)
print(f"{n}! = {result}")
