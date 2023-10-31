'''
Design an algorithm that makes the following exchanges:
                a -->  b --> c           then again ( c --> a )
The arrow indicate that b is to assume the value of a, c the value of b and so on.

'''

# Initial values of a, b and c

a = 'value of a'
b = 'value of b'
c = 'value of c'


# Cyclic exchange

temp = a      # take temporary variable & store value of a  
a = b
b = c 
c = temp

print('a : ', a)
print('b : ', b)
print('c : ', c)