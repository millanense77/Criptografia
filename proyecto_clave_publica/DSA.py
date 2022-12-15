from sympy import randprime, isprime
from random import randint
from math import floor, ceil
from bitarray import bitarray
from bitarray.util import int2ba
import sha1
import pickle
import gammal

def hex2int(x):
    res = '0x' + x
    return eval(res)

def str2ba(m): 
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def escribirFichero(x):
    try:
        output = open("claves_DSA.pkl", 'wb')
        pickle.dump(x,output)
        output.close()
    except:
        print("ERROR: No se pudo escribir el fichero.")

def leerFichero():
    try:
        f=open("claves_DSA.pkl",'rb')
        lectura=pickle.load(f)
        f.close()
        return lectura
    except:
        print("ERROR: No se pudo leer el fichero.")
    return 0


def eleccionQ():
    return randprime(2**159, 2**160)

def eleccionP(Q):
    
    n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
    p = 2 * n * Q + 1
    while(not isprime(p)):
        n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
        p = 2 * n * Q + 1
   
    return p,n

def eleccionG(P,N):

    h = randint(2, P-2) 
    g = pow(h, (2*N), P)
    while(g == 1):
        h = randint(2,P-2) 
        g = pow(h, (2*N), P)
    return g

def generarParametros():
    q = eleccionQ()
    p,n = eleccionP(q)
    g = eleccionG(p,n)
    
    dicc = {}
    dicc['Primo'] = q
    dicc['Grupo'] = p
    dicc['Generador'] = g
    escribirFichero(dicc)


def firma(emisor, m):# añado P y Q
    dicc = leerFichero()

    privada = dicc[emisor][0]
    q = dicc['Primo']
    g = dicc['Generador']
    p = dicc['Grupo']
    k = randint(2, q-2)
    r = pow(g, k, p) % q

    H = hex2int(sha1.SHA1(m))
    s = ((H + privada * r) * pow(k, -1, q)) % q

    return r, s

def verificarFirma(r, s, m, emisor): # añado P y Q
    dicc = leerFichero()
    
    publica = dicc[emisor][1]
    Q = dicc['Primo']
    G = dicc['Generador']
    P = dicc['Grupo']
    
    s = int(s)
    r = int(r)
    w = pow(s,-1,Q)
    H = hex2int(sha1.SHA1(m))
    u1 = H * w % Q
    u2 = r * w % Q
    v = pow(G, u1, P) * pow(publica, u2, P)
    v = (v % P) % Q
    return(v == r)

"""

def generarClavesUsuario(Q,G,P):
    x = randint(1, Q) # aquí iria la clave privada del emisor que va a firmar
    #r, s = firma(G, m, x)
    y = pow(G, x, P) #clave publica
    return x,y
"""

    


