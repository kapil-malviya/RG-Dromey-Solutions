'''
For a given x and a given n, design an algorithm to compute x**n/n! 

'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def output_factorial(x, n):
    if n < 0:
        return None 
    if n == 0:
        return 1.0
    factorial_result = factorial(n)
    x_power_n = x ** n
    result = x_power_n / factorial_result
    return result

x = 2
n = 5
result = output_factorial(x, n)
print(f"{x}^{n}/{n}! = {result}")
