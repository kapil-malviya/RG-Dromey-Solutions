''' 
Implement the Fibonacci algorithm as a function that accepts as input two 
consecutive Fibonacci numbers and returns as output the next Fibonacci number.

'''

def next_fibonacci(a, b):
    return a + b

fibonacci_nums = (0, 1)

next_fib_num = next_fibonacci(*fibonacci_nums)


print(f"next fibonacci number after {fibonacci_nums[0]} and {fibonacci_nums[1]} is: {next_fib_num}")
