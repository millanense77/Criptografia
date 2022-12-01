from sympy import randprime, isprime
from random import randint

q = randprime(1, 2**64)

p = 2 * q + 1

while not isprime(p):
    q = randprime(1, 2**64)
    p = 2 * q + 1

g = 1

a = b = 1 

while (a == 1 and b == 1):
    
    a = pow(g,(p-1)//2,p)
    b = pow(g,(p-1)//q,p)
    
    if(a==1 or b==1):
        g = g + 1
    
privada = randint(1,q-1)
publica = pow(g,privada,p)

print(privada, publica)




