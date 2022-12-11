from sympy import randprime, isprime
from random import randint
from math import floor, ceil
from bitarray import bitarray
from bitarray.util import int2ba
import sha1

#CONSTANTES
Q = randprime(2**159, 2**160)
def eleccionP():
    n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
    p = 2 * n * Q +1
    while(not isprime(p)):
        n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
        p = 2 * n * Q + 1
   
    return p,n

P,N = eleccionP()

def eleccionG():

    h = randint(2, P-2) 
    g = pow(h, (2*N), P)
    while(g == 1):
        h = randint(2,P-2) 
        g = pow(h, (2*N), P)
    return g
G = eleccionG()

def hex2int(x):
    res = '0x' + x
    return eval(res)
def str2ba(m): 
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def firma(g, m, x):
    k = randint(2, Q-2)
    r = pow(g, k, P) % Q
    H = hex2int(sha1.SHA1(str2ba(m)))
    s = ((H + x * r) * pow(k, -1, Q)) % Q
    return r, s

def DSA(m):
    x = randint(1, Q) # aquí iria la clave privada del emisor que va a firmar
    r, s = firma(G, m, x)
    y = pow(G, x, P) #clave publica
    print(y)
    print(r)
    print(s)

def verificarFirma(r, s, m, y):
    w = pow(s,-1,Q)
    H = hex2int(sha1.SHA1(str2ba(m)))
    u1 = H * w % Q
    u2 = r * w % Q
    v = pow(G, u1, P) * pow(y, u2, P)
    v = (v % P) % Q
    return(v == r)



#sha1.SHA1('abc')

"""
Cada usuario -> 0 < x < q aleatorio  -> clave privada

En dos txt aparte
Guardar claves privads y publicas en diccionarios:
Privadas = {Pepe: x, juan: y}
Publicas = {Pepe: gx, juan: gy}
"""
#m = "abc"