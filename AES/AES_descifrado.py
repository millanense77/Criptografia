from bitarray import bitarray
from bitarray.util import hex2ba as h2b, ba2hex as b2h, ba2int as b2i, int2ba as i2b
import AES_cifrado
from AES_cifrado import formatoMsj

def invPerm(e, k):
    """
    Esta funcion realiza una permutacion cíclica de derecha a izquierda
    Recibe un bitarray y el numero de posiciones.
    Devuelve el bitarray permutado.
    """
    E = e.copy()
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
    R = AES_cifrado.arrayToMat(R)
    for i in range(4):
        E.append(invPerm(R[i],i))
    E = AES_cifrado.mat2Array(E)
    return E

def invMixColumns(x):
    """
    Esta funcion realiza la operacion inversa a mixColumn,
    multiplicando cada columna por la matriz
    [[E,B.D,9],[9,E,B,D],[D,9,E,B],[B,9,D,E]]
    Recibe un bitarray
    Devuelve un bitarray
    """
    x = AES_cifrado.transpose(AES_cifrado.arrayToMat(x))
    R = []
    for v in x:
        S = []
        for i in range(4):
            aux = (
                AES_cifrado.xtime(
                    AES_cifrado.xtime(
                        AES_cifrado.xtime(v[0] ^ v[1] ^ v[2] ^ v[3])
                        )) 
                    ^ AES_cifrado.xtime(
                        AES_cifrado.xtime(v[0] ^ v[2])
                        ) ^ 
                        AES_cifrado.xtime(v[0] ^ v[1]) ^ v[1] ^ v[2] ^ v[3]
            )
            #aux = x^3(a+b+c+d) + x^2(a+c) + x(a+b) + b + c + d
            S.append(aux)
            v.append(v[0])
            del(v[0])
        R.append(S)
    R = AES_cifrado.mat2Array(AES_cifrado.transpose(R))
    return R

def AES_des(msj, k):
    """
    Esta es la funcion principal que lleva a cabo
    todo el proceso de descifrado.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    K = AES_cifrado.expand(k)

    E = AES_cifrado.addRoundKey(msj, K[10])

    for i in reversed(range(1,10)):
        E = invShiftRows(E)
        E = AES_cifrado.subByte(E, 128, 1)
        E = AES_cifrado.addRoundKey(b2h(E), K[i])
        E = invMixColumns(E)
        
    E = invShiftRows(E)
    E = AES_cifrado.subByte(E, 128, 1)
    E = AES_cifrado.addRoundKey(b2h(E), K[0])
    return b2h(E)

def CBC_descifrado(msj, key, IV):
    """
    Esta es la funcion principal que lleva a cabo
    todo el proceso de descifrado CBC.
    Recibe un mensaje y una clave en hexadecimal.
    Devuelve una cadena hexadecimal.
    """
    lista = []
    for i in range(0, len(msj),32):
        aux = AES_cifrado.formatoMsj(msj[i:i+32])
        lista.append(aux)
    key = AES_cifrado.formatoMsj(key)
    IV = AES_cifrado.formatoMsj(IV)

    descifrado = b2h(h2b(lista[0]) ^ h2b(IV))
    for i in range(1, len(lista)):
        mensaje = AES_des(lista[i], key)
        descifrado = b2h(h2b(mensaje) ^ h2b(descifrado))
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
    k = formatoMsj(k)
    for i in bloques:
        bloquesDes.append(AES_des(formatoMsj(i),k))
    descifrado = "" 
    for i in bloquesDes:
        descifrado += i
        
    return(descifrado)

