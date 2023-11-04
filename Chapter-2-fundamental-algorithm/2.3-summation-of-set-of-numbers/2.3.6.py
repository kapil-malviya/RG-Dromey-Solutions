'''
Generate the first n terms of the sequence 
    1   2   4   8   16   32   ...
without using multiplication.
 
'''

def generate_sequence(n):
    if n < 0:
        return []

    sequence = [1]             # initialize sequence with the first term
    term = 1

    for _ in range(1, n):
        term = term + term     # double previous term
        sequence.append(term)

    return sequence

n = 28

sequence = generate_sequence(n)

print(sequence)
