'''
Design an algorithm to determine whether or not a number n is a factorial number

'''

def fact_num(n):
    factorial = 1
    i = 1
    while factorial <= n:
        if factorial == n:
            return True
        i += 1
        factorial *= i
    return False

n = 242
result = fact_num(n)
if result:
    print(f'{n} is a factorial number')
else:
    print(f'{n} is not a factorial number')