'''
For a given n, design an algorithm to compute 1/n!

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def inverse_factorial(n):
    if n < 0:
        return None  
    if n == 0:
        return 1.0  # 1/0! = 1
    factorial_result = factorial(n)
    result = 1.0 / factorial_result
    return result

n = 5
inverse_factorial = inverse_factorial(n)
print(f"1/{n}! = {inverse_factorial}")