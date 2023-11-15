'''

Given a=0, b=1 and c=1 are the first three numbers of some sequence. All other numbers 
in the sequence are generated from the sum of their three most recent predecessors. 
Design an algorithm to generate this sequence.

'''


def generate_sequence(n):
    sequence = [0, 1, 1]              # initial values

    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_term)

    return sequence

n_terms = 10
sequence = generate_sequence(n_terms)

print(f"first {n_terms} terms of the sequence are: {sequence}")
