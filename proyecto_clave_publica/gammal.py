from bitarray import bitarray
from bitarray.util import ba2int, int2ba
from sympy import randprime, isprime
from random import randint
import pickle

#Helpers
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

def str2int(m):
    """
    Este metodo convierte un string en un numero entero.
    Recibe una cadena de texto.
    Devuelve un numero entero.
    """
    return(ba2int(str2ba(m)))

def int2txt(n):
    """
    Este metodo convierte un numero entero en un string.
    Recibe un numero entero.
    Devuelve una cadena de texto.
    """
    res = int2ba(n)
    while(len(res)%8 !=0):
        res = bitarray('0') + res
    bloques = []
    for i in range(0, len(res), 8):
        bloques.append(chr(ba2int(res[i:i+8])))
    res = ''
    return (res.join(bloques))

def escribirFichero(x):
    """
    Este metodo crea un fichero binario con el
    contenido que se le indique.
    Recibe un tipo de dato sin especificar.
    No devuelve nada.
    """
    try:
        output = open("./claves_Gammal.pkl", 'wb')
        pickle.dump(x,output)
        output.close()
    except:
        print("ERROR: No se ha podido escribir el fichero.")

def leerFichero():
    """
    Este metodo lee un fichero binario y recoje
    su contenido.
    No recibe nada.
    Devuelve el contenido del fichero.
    """
    try:
        f=open("claves_Gammal.pkl",'rb')
        lectura=pickle.load(f)
        f.close()
        return lectura
    except:
        print("ERROR: No se ha podido leer el fichero.")
    return 0

#Generacion de Claves
#Administrador
def generarGrupo(q):
    """
    Este metodo crea un grupo multiplicativo finito.
    Recibe un numero entero.
    Devuelve un numero entero.
    """
    p = 2 * q + 1
    while not isprime(p):
        q = randprime(2**159, 2**160)  
        p = 2 * q + 1
    return p

def generarGenerador(p,q):
    """
    Este metodo calcula un numero generador
    perteneciente al grupo finito.
    Recibe dos numeros enteros.
    Devuelve un numero entero.
    """
    g = 1
    a = b = 1 
    while(a == 1 and b == 1):
        a = pow(g, (p-1)//2, p)
        b = pow(g, (p-1)//q, p)
        if(a==1 or b==1):
            g = g + 1
    return g

def generarParametros():
    """
    Este metodo crea los parametros necesarios
    para el algoritmo ElGamal, los guarda en un fichero
    y devuelve True si todo ha ido bien o False en caso contrario.
    No recibe ningun parametro.
    Devuelve un booleano.
    """
    try:
        q = randprime(2**1023, 2**1024)
        p = generarGrupo(q)
        g = generarGenerador(p,q)

        dicc = {}
        dicc['Grupo'] = p
        dicc['Generador'] = g
        escribirFichero(dicc)
        return True
    except:
        return False

def cifrarMensaje(dest, m):
    """
    Este metodo cifra un mensaje de texto recibido para 
    ser enviado al destinatario deseado aplicando
    el algoritmo de ElGamal.
    Recibe un numero entero y una cadena de texto.
    Devuelve dos numero enteros.
    """
    dicc = leerFichero()
    p = dicc['Grupo']
    g = dicc['Generador']
    publica = dicc[dest][1]

    v = randint(1, 2*64) % p
    V = pow(g,v,p)
    x = pow(publica,v, p)
    c = (str2int(m) * x)
    return (V,c)

def descifrarMensaje(usuario, V, c):
    """
    Este metodo descifra un mensaje recibido
    aplicando el algoritmo de ElGammal.
    Recibe tres numeros enteros.
    Devuelve una cadena de texto.
    """
    dicc = leerFichero()
    y = pow(int(V),dicc[usuario][0],dicc['Grupo'])
    m = int(c) // y
    return int2txt(m)



