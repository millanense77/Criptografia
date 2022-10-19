from bitarray import bitarray
from bitarray.util import hex2ba as h2b, ba2hex as b2h, ba2int as b2i, int2ba as i2b
from functools import reduce as reduce

def addRoundKey(E, k):
    """
    Esta funcion realiza la operacion XOR entre dos bitarray.
    Recibe dos parametros en hexadecimal.
    Devuelve el bitarray resultante.
    """
    e = h2b(E)
    Kb = h2b(k)
    X = e ^ Kb
    return X


def subByte(b):
    """
    Esta funcion utiliza los 4 primeros bits para establecer la fila
    y los 4 ultimos para la columna. Devuelve el numero que concuerde con 
    la fila y la columna.
    Recibe un bitarray de tamaño 8.
    Devuelve un bitarray de tamaño 8.
    """
    s = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
    ]
    
    x = b[:4]
    y = b[4:]
    x = b2i(x)
    y = b2i(y)
    res = s[x][y]
    res = i2b(res)
    while(len(res)<8):
        res = bitarray('0')+res
    return res

def Sbox(E, tam):
    """
    Esta funcion divide el bitarray en partes de 8 bits, que las pasa
    a la funcion subByte, y concatena en un bitarray el bitarray
    devuelto por la funcion subByte(la caja).
    Recibe como parametros un bitarray y la longitud del bitarray.
    Devuelve el bitarray resultante.
    """
    B = bitarray()
    for i in range(0, tam, 8):
        b = E[i:i+8]
        b = subByte(b)
        B += b
    return B


def mat2Array(M):
    """
    Esta funcion convierte una matriz 4x4 en un bitarray
    Recibe una matriz 4x4.
    Devuelve un bitarray.
    """
    R = bitarray()
    for i in range(4):
        for j in range(4):
            R = R + M[j][i]
    return R

def arrayToMat(E):
    """
    Esta funcion convierte un bitarray en una matriz 4x4.
    Recibe un bitarray.
    Devuelve una matriz 4x4.
    """
    L = []
    for i in range(0,128,8):
        L.append(E[i:i+8])
    R = []
    for i in range(4):#Columnas
        fila = []
        for j in range(4):#Filas
            fila.append(L[i+4*j])
        R.append(fila)
    return R

def perm(e, k):
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

def  shiftRows(E):
    """
    Esta funcion llama a las funciones arrayToMat y perm
    Recibe un bitarray.
    Devuelve una matriz 4x4.
    """
    E = arrayToMat(E)
    R = []
    for i in range(4):
        R.append(perm(E[i],i))
    R = mat2Array(R)
    return R


def transpose(E):
    """
    Esta funcion hace la trasposicion de una matriz.
    Recibe una matriz 4x4.
    Devuelve una matriz 4x4.
    """
    R = []
    for i in range(4):
        aux = []
        for j in range(4):
            aux.append(E[j][i])
        R.append(aux)
    return R
#Sin descripcion
def xtime(b):
    """
    Esta funcion 
    Recibe un bitarray.
    Devuelve un bitarray.
    """
    b.append(0)
    if(b[0]==1):
        b ^= bitarray('100011011')
    del[b[0]]
    return b
#Sin descripcion
def mult(v):
    """
    Esta funcion 
    Recibe una lista con bitarrays.
    Devuelve una lista con bitarrays.
    """
    R = []
    for i in range(4):
        aux = xtime(v[0] ^ v[1]) ^ v[1] ^ v[2] ^ v[3]
        #aux = xtime(v[0]) ^ xtime(v[1]) ^ v[2] ^ v[3]
        R.append(aux)
        v.append(v[0])
        del(v[0])
    return R

#Sin descripcion
def mixColumns(E):
    """
    Esta funcion 
    Recibe una matriz 4x4.
    Devuelve un bitarray.
    """
    E = arrayToMat(E)
    E = transpose(E)#Cada lista es una columna de la matriz
    R = []
    for v in E:
        w = mult(v)
        R.append(w)
    R = transpose(R)#Cada lista es una fila de la matriz
    R = mat2Array(R)
    return R


def trozos(a):
    """
    Esta funcion separa un bitarray de tamaño 128 en 4 trzos de 32 bits.
    Recibe un bitarray.
    Devuelve una lista con 4 bitarrays.
    """
    res = []
    for i in range(0,128,32):
        res.append(a[i:i+32])
    return res

def expand(k):
    """
    Esta funcion genera diez claves diferentes a partir de una clave.
    Recibe la clave en hexadecimal.
    Devuelve una lista de claves en hexadecimal.
    """
    C = ['01000000', '02000000', '04000000', '08000000', '10000000',
        '20000000', '40000000', '80000000', '1B000000', '36000000']
    K = []
    K.append(h2b(k))
    for i in range(10):
        previa = K[-1]#Ultima posicion del conjunto de claves => K[3]
        Previa = trozos(previa)#divide 128 bits en 4 trozos de 32 bits = << 8
        aux = Previa[3]
        aux = perm(aux, 8)#Rotacion circular de 8 bits a la izquierda
        aux = Sbox(aux, 32)
        aux = aux ^ h2b(C[i]) ^ Previa[0] 
        L =[]
        L.append(aux)
        for j in range(3):
            aux = Previa[j+1] ^ aux
            L.append(aux)
        sig = reduce(lambda x,y: x+y, L)
        K.append(sig)
    res = []
    for i in range(len(K)):
        res.append(b2h(K[i]))
    return res


def AES_impreso(msj, k):
    K = expand(k)
    print('Las claves generadas son: ')
    for i in range(10):
        print('Clave '+str(i)+': '+str(K[i]))
    E = addRoundKey(msj, K[0])
    E = b2h(E)
    print('\ni = 0: start= '+str(msj))
    E = h2b(E)
    for r in range(1,11):
        E = Sbox(E, 128)
        E = b2h(E)
        print('i = '+str(r)+': sbox= '+str(E))
        E = h2b(E)
        E = shiftRows(E)
        E = b2h(E)
        print('i = '+str(r)+': shift= '+str(E))
        E = h2b(E)
        if(r<10):
            E = mixColumns(E)
            E = b2h(E)
            print('i = '+str(r)+': mixColumn= '+str(E))
            E = h2b(E)
        E = b2h(E)
        E = addRoundKey(E, K[r])
        E = b2h(E)
        print('\n')
        print('i = '+str(r)+'ksch: '+str(K[r]))
        print('i = '+str(r+1)+': start= '+str(E))
        E = h2b(E)
    E = b2h(E)
    return E

#msj = 32 cifras en hexadecimal
#k = clave de 32 cifras en hexadecimal
# devuelve 32 cifras hexadecimales
def AES128(msj, k):
    """
    Funcion principal del algortimo, desde la que se lanza todo el proceso.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    K = expand(k)
    E = addRoundKey(msj, K[0])
    for r in range(1, 10):
        E = Sbox(E, 128)
        E = shiftRows(E)
        if(r<10):
            E = mixColumns(E)
        E = b2h(E)
        E = addRoundKey(E, K[r])
    return E

#AES_impreso('00112233445566778899aabbccddeeff','000102030405060708090a0b0c0d0e0f')

def invShiftRows(R):  #recibo la matriz 4x4
    """
    Esta funcion recibe una matriz 4x4 y devuelve un bitarray
    """
    E = []
    #convierto la matrix 4x4 en un bitarray
    for i in range(4):
        E.append(invPerm(R[i],i))    
    E = mat2Array(E)
    return E


def invPerm(e, k):
    """
    Esta funcion realiza una permutacion cíclica de derecha a izquierda
    Recibe un bitarray y el numero de posiciones.
    Devuelve el bitarray permutado.
    """
    E = e.copy()  #E es la fila de la matrix 4x4 y k es el elemento de la fila
    for i in range(k):
        E.insert(0,E[len(E) - 1])
        del(E[len(E) - 1])
    return E

def invMixColumns(E):
    E = arrayToMat(E)
    E = transpose(E)
    R = []
    for v in E:
        w = mult(v)
        R.append(w)
    R = transpose(R)
    R = mat2Array(R)
    return R

def invMult(v):
    
    S = []
    
    S0 = mult0E(v[0]) ^ mult0B(v[1]) ^ mult0D(v[2]) ^ mult09(v[3])
    S1 = mult09(v[0]) ^ mult0E(v[1]) ^ mult0B(v[2]) ^ mult0D(v[3])
    S2 = mult0D(v[0]) ^ mult09(v[1]) ^ mult0E(v[2]) ^ mult0B(v[3])
    S3 = mult0B(v[0]) ^ mult0D(v[1]) ^ mult09(v[2]) ^ mult0E(v[3])
    
    S.append(S0)
    S.append(S1) 
    S.append(S2)
    S.append(S3)
        
    return S

def mult09(b):
    a = xtime(xtime(xtime(b)))
    return(a ^ b)

def mult0E(b):
    a = xtime(b)
    c = xtime(a)
    d = xtime(c)
    return(a ^ b ^ c)

def mult0B(b):
    a = xtime(b)
    c = xtime(xtime(a))
    return(a ^ b ^ c)

def mult0D(b):
    a = xtime(xtime(b))
    c = xtime(a)
    return(a ^ b ^ c)