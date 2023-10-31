'''
Develop an algorithm that prints out n values of the sequence
        1   -1   1   -1   1   -1   ...

'''

def sequence(n):
    for i in range(n):
        if i % 2 == 0:
            print(1, end=' ')
        else:
            print(-1, end=' ')

n = 8
sequence(n)