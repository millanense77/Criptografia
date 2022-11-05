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


def sBox(b, opcion):
    """
    Esta funcion utiliza los 4 primeros bits para establecer la fila
    y los 4 ultimos para la columna. Devuelve el numero que concuerde con 
    la fila y la columna.
    Recibe un bitarray de tamaño 8 y la opcion de cifrado (0) o descifrado (1).
    Devuelve un bitarray de tamaño 8.
    """
    sbox = [
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
    invSBox = [
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
    ]
    
    x = b[:4]
    y = b[4:]
    x = b2i(x)
    y = b2i(y)
    if(opcion == 0):
        res = sbox[x][y]
    else:
        res = invSBox[x][y]
    res = i2b(res)
    while(len(res)<8):
        res = bitarray('0')+res
    return res

def subByte(E, tam, opcion):
    """
    Esta funcion divide el bitarray en partes de 8 bits, que las pasa
    a la funcion sBox, y concatena en un bitarray el bitarray
    devuelto por la funcion sBox(la caja).
    Recibe como parametros un bitarray, la longitud del bitarray 
    y la opcion si es cifrado (0) o descifrado (1).
    Devuelve el bitarray resultante.
    """
    B = bitarray()
    for i in range(0, tam, 8):
        b = E[i:i+8]
        b = sBox(b, opcion)
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

def xtime(b):
    """
    Esta funcion realiza la operacion xtime,
    si el termino de grado 7 del polinomio es 1, se reduce el polinomio 
    dividiendolo (hace XOR) con el polinomio irreducible m(x), 
    siendo m(x) = x^8+x^4+x^3+x+1, si es 0 hace un desplazamiento
    a la izquierda.
    Recibe un bitarray.
    Devuelve un bitarray.
    """
    b.append(0)
    if(b[0]==1):
        b ^= bitarray('100011011')
    del[b[0]]
    return b

def mult(v):
    """
    Esta funcion multiplica la columna por
    la matriz [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    Recibe una lista con bitarrays.
    Devuelve una lista con bitarrays.
    """
    R = []
    for i in range(4):
        aux = xtime(v[0] ^ v[1]) ^ v[1] ^ v[2] ^ v[3] #x(a+b)+b+c+d
        R.append(aux)
        v.append(v[0])
        del(v[0])
    return R

def mixColumns(E):
    """
    Esta funcion aplica a cada columna la misma transformacion lineal
    llamando a la funcion mult().
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
        Previa = trozos(previa)
        aux = Previa[3]
        aux = perm(aux, 8)#Rotacion circular de 8 bits a la izquierda
        aux = subByte(aux, 32, 0)
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

  
def AES_cif(msj, k):
    """
    Funcion principal del algortimo, desde la que se lanza 
    todo el proceso de cifrado.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    K = expand(k)
    E = addRoundKey(msj, K[0])
    for r in range(1, 11):
        E = subByte(E, 128, 0)
        E = shiftRows(E)
        if(r<10):
            E = mixColumns(E)
        E = b2h(E)
        E = addRoundKey(E, K[r])
    return b2h(E)

def stringToHexadecimal(msj):
    res = ''
    for i in msj:
        aux = hex(ord(i))
        res += aux[2:]
    res = res[6:]
    return res

def CBC_cifrado(msj, key):
    """
    Esta es la funcion desde la que se lanza 
    todo el proceso de cifrado CBC.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    IV = stringToHexadecimal('ALONSOCARLOSFERNAND')
    input = b2h(h2b(msj) ^ h2b(IV))
    cifrado = AES_cif(input, key)
    return cifrado

def ECB_cifrado(cadena,k):
    """
    Esta es la funcion desde la que se lanza 
    todo el proceso de cifrado ECB.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    bloques = []
    for i in range(0,len(cadena),128):
        bloques.append(cadena[i:i+128])
        
    bloquesCif = []
    for i in bloques:
        bloquesCif.append(AES_cif(i,k))
    cifrado = "" 
    for i in bloquesCif:
        cifrado += i
        
    return(cifrado)

"""
               ------------ 
                DESCIFRADO
               ------------ 
"""
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

def invShiftRows(R):
    """
    Esta funcion llama a la funcion arrayToMat, invPerm y mat2Array
    Recibe un bitarray
    Devuelve un bitarray
    """
    E = []
    R = arrayToMat(R)
    for i in range(4):
        E.append(invPerm(R[i],i))    
    E = mat2Array(E)
    return E

def invMixColumns(x):
    """
    Esta funcion realiza la operacion inversa a mixColumn,
    multiplicando cada columna por la matriz
    [[E,B.D,9],[9,E,B,D],[D,9,E,B],[B,9,D,E]]
    Recibe un bitarray
    Devuelve un bitarray
    """
    x = transpose(arrayToMat(x))
    R = []
    for v in x:
        S = []
        for i in range(4):
            aux = xtime(xtime(xtime(v[0] ^ v[1] ^ v[2] ^ v[3]))) ^ xtime(xtime(v[0] ^ v[2])) ^ xtime(v[0] ^ v[1]) ^ v[1] ^ v[2] ^ v[3]
            # x^3(a+b+c+d) + x^2(a+c) + x(a+b) + b + c + d
            S.append(aux)
            v.append(v[0])
            del(v[0])
        R.append(S)
    R = mat2Array(transpose(R))
    return R

def AES_des(msj, k):
    """
    Esta es la funcion principal que lleva a cabo
    todo el proceso de descifrado.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    K = expand(k)

    E = addRoundKey(msj, K[10])

    for i in reversed(range(1,10)):
        E = invShiftRows(E)
        E = subByte(E, 128, 1)
        E = addRoundKey(b2h(E), K[i])
        E = invMixColumns(E)
        
    E = invShiftRows(E)
    E = subByte(E, 128, 1)
    E = addRoundKey(b2h(E), K[0])
    return b2h(E)

def CBC_descifrado(msj, key):
    """
    Esta es la funcion principal que lleva a cabo
    todo el proceso de descifrado CBC.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    IV = stringToHexadecimal('ALONSOCARLOSFERNAND')
    input = AES_des(msj, key)
    descifrado = b2h(h2b(input) ^ h2b(IV))
    return descifrado

def invECB(cadena,k):
    """
    Esta es la funcion principal que lleva a cabo
    todo el proceso de descifrado ECB.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    bloques = []
    for i in range(0,len(cadena),128):
        bloques.append((cadena[i:i+128]))   
    bloquesDes = []
    for i in bloques:
        bloquesDes.append(AES_des(i,k))
    descifrado = "" 
    for i in bloquesDes:
        descifrado += i
        
    return(descifrado)

def formatoMsj(txt):
    """
    Esta es la funcion comprueba que el formato de la cadena
    que recibe es el correto (longitud 32 y en hexadecimal).
    Recibe una cadena de texto.
    Devuelve True si es correcta o False si no esta bien.
    """
    if(len(txt)<32 or len(txt)>32):
        print('La cadena debe tener 32 bytes de longitud.')
        return False
    try:
        int(txt, 16)
    except: 
        print('La cadena debe ser en hexadecimal')
        return False
    
    return True

def main():
    #Introduccion y comprobacion del mensaje
    flag = False
    while(flag == False):
        msj = input('Introduzca un mensaje en hexadecimal de 32 bytes: ')
        flag = formatoMsj(msj)
    #Introduccion y comprobacion de la clave
    flag = False
    while(flag == False): 
        key = input('Introduzca una clave en hexadeciaml de longitud maxima 32 bytes: ')
        aux = key
        if(len(aux)<32):
            i = 0
            while(len(aux)<32):
                aux += aux[i]
                i = i + 1
        flag = formatoMsj(aux)
        
    print('\nMensaje sin cifrar: '+str(msj))
    print("Clave: "+str(key))
    
    CBC = CBC_cifrado(msj, aux)
    print('\nCifrado con CBC: '+str(CBC))
    CBC = CBC_descifrado(CBC,aux)
    print('\nDescifrado con CBC: '+str(CBC))

    ECB = ECB_cifrado(msj, aux)
    print('\nCifrado con ECB: '+str(ECB))
    ECB = invECB(ECB,aux)
    print('\nDescifrado con ECB: '+str(ECB))

main()

#main('00112233445566778899aabbccddeeff','000102030405060708090a0b0c0d0e0f')

#msj = '00112233445566778899aabbccddeeff'
#key = '000102030405060708090a0b0c0d0e0f'