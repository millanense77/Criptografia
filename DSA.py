from sympy import randprime, isprime
from random import randint
from math import floor, ceil

q = randprime(2**159, 2**160)

n = randint(ceil((2**1023 -1)/(2*q)), floor((2**1024-1)/(2**q)))
p = 2 * n * q +1

while not isprime(p):
    n = randint(ceil((2**1023 -1)/(2*q)), floor((2**1024-1)/(2**q)))
    p = 2 * n * q + 1
    
h = randint(2,p-2) 
g = pow(h,2*n,p)

while g == 1:
    h = randint(2,p-2) 
    g = pow(h,2*n,p)
    
y = pow(g,x,p) #clave publica

"""
Cada usuario -> 0 < x < q aleatorio  -> clave privada
"""

k = randint(2, q-2)
r = pow(g,k,p) % q
H = hextoint(SHA1(m))
s = ((H + x * r) * pow(k,-1,q)) % q


w = pow(s,-1,q)
u1 = H * w % q
u2 = r * w % q
v = pow(g,u1,p) * pow(y,u2,p)
v = (v % p) % q
    
print(v == r)

