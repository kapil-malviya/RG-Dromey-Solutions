'''
The first few numbers of the Lucas sequence which is a variation on the Fibonacci sequence are : 
    1  3  4  7  11  18  29 ...
Design an algorithm to generate the Lucas sequence.

''' 

def lucas_seq(n):
    lucas_sequence = [2, 1] 

    while len(lucas_sequence) < n:
        next_term = lucas_sequence[-1] + lucas_sequence[-2]
        lucas_sequence.append(next_term)

    return lucas_sequence

n_terms = 10
lucas_sequence = lucas_seq(n_terms)

print(f"the first {n_terms} terms of Lucas sequence are: {lucas_sequence}")
