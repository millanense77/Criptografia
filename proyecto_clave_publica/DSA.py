from sympy import randprime, isprime
from random import randint
from math import floor, ceil
from bitarray import bitarray
from bitarray.util import int2ba
import sha1
import pickle
import gammal

#CONSTANTES

def eleccionQ():
    return randprime(2**159, 2**160)

def eleccionP():
    Q = eleccionQ()
    n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
    p = 2 * n * Q + 1
    while(not isprime(p)):
        n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
        p = 2 * n * Q + 1
   
    return p,Q,n


def eleccionG(P,N):

    h = randint(2, P-2) 
    g = pow(h, (2*N), P)
    while(g == 1):
        h = randint(2,P-2) 
        g = pow(h, (2*N), P)
    return g


def generarParametros():
  
    dicc = leerFichero()
    if 'Primo' in dicc: # si Q ya esta creada, se coge del fichero del gammal
        q = dicc['Primo']
        
    else: 
        q = eleccionQ()  
    
    p,n = eleccionP(q)
    g = eleccionG(p,n)
    
    dicc = {}
    dicc['Primo'] = q
    dicc['Grupo'] = p
    dicc['Generador'] = g
    print(dicc)
    escribirFichero(dicc)

def escribirFichero(x):
    output = open("claves_DSA.pkl", 'wb')
    pickle.dump(x,output)
    output.close()

def leerFichero():
    f=open("claves_DSA.pkl",'rb')
    lectura=pickle.load(f)
    f.close()
    return lectura
    

def hex2int(x):
    res = '0x' + x
    return eval(res)

def str2ba(m): 
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def firma(g, m, x, P, Q):# añado P y Q
    k = randint(2, Q-2)
    r = pow(g, k, P) % Q
    H = hex2int(sha1.SHA1(m))
    s = ((H + x * r) * pow(k, -1, Q)) % Q
    return r, s


"""

def generarClavesUsuario(Q,G,P):
    x = randint(1, Q) # aquí iria la clave privada del emisor que va a firmar
    #r, s = firma(G, m, x)
    y = pow(G, x, P) #clave publica
    return x,y
"""

def verificarFirma(r, s, m, y, P, Q, G): # añado P y Q
    s = int(s)
    r = int(r)
    w = pow(s,-1,Q)
    H = hex2int(sha1.SHA1(m))
    u1 = H * w % Q
    u2 = r * w % Q
    v = pow(G, u1, P) * pow(y, u2, P)
    v = (v % P) % Q
    return(v == r)

    


