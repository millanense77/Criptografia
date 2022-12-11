from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex, ba2int, int2ba

HASH = hex2ba("67452301EFCDAB8998BADCFE10325476C3D2E1F0")

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

#Padding
def padding(b):
    """
    Este metodo crea un bitarray de tamaño 
    multiplo de 512.
    Recibe un bitarray.
    Devuelve un bitarray de tamaño multiplo 512.
    """
    tam = len(b) #Tamaño del bitarray original
    L = tam - (tam//512*512) #Tamaño del ultimo bloque si se divide en bloques de 512 bits
    #Si el ultimo bloque es mayor o igual a 448 calcula k0 creando un bloque mas
    #Si no calcula k0 rellenando el que hay.
    if(L % 512 < 448): k = 448-L-1
    else: k = 960-L-1
    B = b.copy()
    B += bitarray('1')
    k0 = bitarray('0') * k
    B += k0

    B = B + int2ba(tam,64)
    return B

def parsing(mensaje, bits):
    """
    Esta funcion divide enel mensaje en bloques
    de N bits.
    Recibe un bitarray y el tamaño de los bloques.
    Devuelve una lista con los bloques.
    """
    bloques = []
    for i in range(0,len(mensaje),bits):
        bloques.append((mensaje[i:i+bits]))
    return bloques

def ROTL(e, k):
    """
    Esta funcion permuta tantas posiciones como se le indice a la izquierda
    Recibe un bitarray y el numero de posiciones.
    Devuelve el bitarray permutado.
    """
    E = e.copy()
    for i in range(k):
        E.append(E[0])
        del(E[0])
    return E

def expand(bloque):
    w = []
    for i in range(0,512,32):
        w.append(bloque[i:i+32])
    for i in range(16,80):
        w.append(ROTL(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
    return w

def funcNoLineal(i, B, C, D):
    """
    Esta funcion realiza la operacion no lineal correspondiente a la vuelta
    Recibe el nº de vuelta, y las variables BB, CC y DD.
    Devuelve el resultado de la operacion correspondiente.
    """
    if 0 <= i <= 19:
        f = (B & C) | ((~B) & D) 
    else:
        if 20 <= i <= 39:
            f = B ^ C ^ D
        else :
            if 40 <= i <= 59:
                f = (B & C) | (B & D) | (C & D) 
            else:
                if 60 <= i <= 79:
                    f = B ^ C ^ D
    return f

def constante(i):
    """
    Esta funcion genera la constante correspondiente a la vuelta.
    Recibe el nº de vuelta.
    Devuelve la constante correspondiente.
    """
    if 0 <= i <= 19:
        return hex2ba('5A827999')
    else:
        if 20 <= i <= 39:
            return hex2ba('6ED9EBA1')
        else :
            if 40 <= i <= 59:
                return hex2ba('8F1BBCDC')
            else:
                if 60 <= i <= 79:
                    return hex2ba('CA62C1D6')


def sha1(hash, bloque):
    w = expand(bloque)
    AA = hash[0:32]
    BB = hash[32:32*2]
    CC = hash[32*2:32*3]
    DD = hash[32*3:32*4]
    EE = hash[32*4:32*5]
    
    for i in range(80):
        T = (ba2int(ROTL(AA,5)) + ba2int(funcNoLineal(i, BB, CC, DD)) + ba2int(EE) + ba2int(w[i]) + ba2int(constante(i))) % 2**32
        EE = DD
        DD = CC
        CC = ROTL(BB, 30)
        BB = AA
        AA = int2ba(T,32)

    AA = (ba2int(AA) + ba2int(hash[0:32])) % 2**32
    BB = (ba2int(BB) + ba2int(hash[32:32*2])) % 2**32
    CC = (ba2int(CC) + ba2int(hash[32*2:32*3])) % 2**32
    DD = (ba2int(DD) + ba2int(hash[32*3:32*4])) % 2**32
    EE = (ba2int(EE) + ba2int(hash[32*4:32*5])) % 2**32

    res = int2ba(AA,32)+int2ba(BB,32)+int2ba(CC,32)+int2ba(DD,32)+int2ba(EE,32)

    return res

def SHA1(mensaje):
    
    mensaje = padding(hex2ba(str2hex(mensaje)))
    lista = parsing(mensaje,512)
    hash = HASH
    for bloque in lista:
        hash = sha1(hash, bloque)
    
    return ba2hex(hash)


#msj = hex2ba(str2hex('abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'))
#print(SHA1(msj))
#h = str2hex(msj)
#b = hex2ba(h)
#x = padding(b)
#y = parsing(x, 512)
