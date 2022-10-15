
#M = String de 32 caracteres
#k = string 32 cifras hexadecimales

from bitarray.util import hex2ba, ba2hex, ba2int, int2ba
from bitarray import bitarray

def AES(M,k):
    K = expand(k)
    m = hex2ba(M)
    Kb = hex2ba(K[0])
    E = m ^ Kb
    for r in range(1,10):
        E = Sbox(E)
        E = shiftRows(E)
        E = mixColumns(E)
        E = E ^ hex2ba(K[r])
        E = Sbox(E)
        E = shiftRows(E)
        E = E ^ hex2ba(K[10])
        E = ba2hex(E)
        return(E)

def sbox(b):
    x = b[:4] 
    y = b[4:]
    
    x = ba2int(x)
    y = ba2int(y)
    
    resultado = Tabla[x,y] 
    res = hex2ba(resultado)
    
    return(res)
    
def Sbox(E):
    B = bitarray()
    for i in range(0,128,8):
        b= E[i:i+8]
        b = sbox(b)
        B += b
    return(B)

def shiftRows(E):
    E = array2mat(E)
    R = []
    for i in range(4):
        R.append(perm([i],i))# funcion de permutacion
    return(mat2array(R))

def array2mat(E):
    L = []
    for i in range(0,128,8):
        L.append(E[i:i+8])
    R = []
    for i in range(4):
        fila = []
        for j in range(4):
            fila.append(L[i+4*j])
        R.append(fila)
    return(R)

def mat2array(E):
    B = bitarray()
    for j in range(4):
        for i in range(4):
            B += E[i][j]
    return(B)

def perm(fila,k):
    res = fila.copy()
    for i in range(k):
        res.append(res[0])
        del(res[0])
    return(res)

def mixColumns(E):
    E = array2mat(E)
    E = transpose(E) #funcion que transponga la matriz
    R = []
    for v in E:
        w = mult(v) # multiplicar por la matirz constante
        R.append(w)
    R = transpose(R)
    R = mat2array(R)
    return(R)

def transpose(E):
    R = []
    for i in range (4):
        col = []
        for j in range (4):
            col.append(E[j][i])
        R.append(col)
    return(R)

def mult(c):
    res = []
    for i in range(4):
        x = xtime(c[0]) ^ xtime(c[1]) ^ c[1] ^ c[2] ^ c[3]
        res.append(x)
        c.append(c[0])
        del(c[0])
    return(res)

def xtime(b):
    b.append(0)
    if b[0] == 1:
        b ^= bitarray('100011011')
    del(b[0])
    return(b)

def expand(k):
    K = []
    K.append(k)
    for i in range (10):
        previa = K[-1]
        Previa = Trozos(previa)
        