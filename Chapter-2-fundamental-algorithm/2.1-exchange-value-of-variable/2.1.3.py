'''

Design an algorithm that makes the following exchanges:
            a <-- b <-- c <-- d                a --> d

'''

# Initial values of a, b, c, and d

a = "value of a"
b = "value of b"
c = "value of c"
d = "value of d"

# Perform the cyclic exchange

temp = d
d = c 
c = b
b = a
a = temp


print('a : ', a)
print('b : ', b)
print('c : ', c)
print('d : ', d)