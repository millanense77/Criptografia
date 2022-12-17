from sympy import randprime, isprime
from random import randint
from math import floor, ceil
from bitarray import bitarray
from bitarray.util import int2ba
import sha1, pickle

def hex2int(x):
    """
    Este metodo convierte un numero hexadecimal en un numero entero.
    Recibe una cadena de texto.
    Devuelve un numero hexadecimal.
    """
    res = '0x' + x
    return eval(res)

def str2ba(m):
    """
    Este metodo convierte un string en un bitarray.
    Recibe una cadena de texto.
    Devuelve un bitarray.
    """
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def escribirFichero(x):
    """
    Este metodo crea un fichero binario con el
    contenido que se le indique.
    Recibe un tipo de dato sin especificar.
    No devuelve nada.
    """
    try:
        output = open("claves_DSA.pkl", 'wb')
        pickle.dump(x,output)
        output.close()
    except:
        print("ERROR: No se pudo escribir el fichero.")

def leerFichero():
    """
    Este metodo lee un fichero binario y recoje
    su contenido.
    No recibe nada.
    Devuelve el contenido del fichero.
    """
    try:
        f=open("claves_DSA.pkl",'rb')
        lectura=pickle.load(f)
        f.close()
        return lectura
    except:
        print("ERROR: No se pudo leer el fichero.")
    return 0


def eleccionQ():
    """
    Este metodo genera un numero primo aleatorio.
    No recibe ningun parametro.
    Devuelve un numero entero.
    """
    return randprime(2**159, 2**160)

def eleccionP(Q):
    """
    Este metodo crea un grupo multiplicativo finito.
    Recibe un numero entero.
    Devuelve dos numeros enteros.
    """
    n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
    p = 2 * n * Q + 1
    while(not isprime(p)):
        n = randint(ceil((2**(1023 -1))/(2*Q)), floor((2**(1024-1))/(2*Q)))
        p = 2 * n * Q + 1
   
    return p,n

def eleccionG(P,N):
    """
    Este metodo calcula un numero generador
    perteneciente al grupo finito.
    Recibe dos numeros enteros.
    Devuelve un numero entero.
    """
    h = randint(2, P-2) 
    g = pow(h, (2*N), P)
    while(g == 1):
        h = randint(2,P-2) 
        g = pow(h, (2*N), P)
    return g

def generarParametros():
    """
    Este metodo crea los parametros necesarios
    para el algoritmo DSA y los guarda en un fichero.
    No recibe ningun parametro.
    Devuelve un booleano.
    """
    try:
        q = eleccionQ()
        p,n = eleccionP(q)
        g = eleccionG(p,n)
        
        dicc = {}
        dicc['Primo'] = q
        dicc['Grupo'] = p
        dicc['Generador'] = g
        escribirFichero(dicc)
        return True
    except:
        return False


def firma(emisor, m):
    """
    Este metodo permite al usuario firmar un mensaje
    aplicando el algoritmo DSA.
    Recibe un numero entero y una cadena de texto.
    Devuelve dos numeros enteros.
    """
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

def verificarFirma(r, s, m, emisor):
    """
    Este metodo comprueba si una firma es verdadera o falsa,
    aplicando el algoritmo DSA.
    Recibe tres numeros enteros y una cadena de texto.
    Devuelve un booleano.
    """
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



