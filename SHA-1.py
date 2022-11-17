"""
Bucle principal: 512 bits -> 160 bits
En general:
1. Padding - multiplos de 512 bits
2. Parsing 
3. Hash 
"""
from bitarray import bitarray
from bitarray.util import ba2hex 
from bitarray.util import ba2int
from bitarray.util import hex2ba
from bitarray.util import int2ba 

HASH = hex2ba("67452301EFCDAB8998BADCFE10325476")

def str2ba(m): 
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def str2int(m):
    return(ba2int(str2ba(m)))

def str2hex(m):
    return(ba2hex(str2ba(m)))

def padding(M):
    L = len(M) + 1 
    K = (448 - L)
    m = M
    if (L < 448):
        E  = 448 - L 
    k0 = bitarray('0') * E
    m = str2ba(m)
    m += bitarray('1') + k0 + int2ba(L-1, 64)
    return(m)
    
def parsing(mensaje, bits):
    bloques = []
    for i in range(0,len(mensaje),bits):
        bloques.append((mensaje[i:i+bits]))
    return bloques
   
def SHA1(mensaje):
    mensaje = padding(mensaje)
    lista = parsing(mensaje,512)
    return(lista)
    """hash = HASH
    for bloque in lista:
        hash = sha1(hash,bloque)
    return(hash)"""

def sha1(ini,bloque):
    pass
    
    
