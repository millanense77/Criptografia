from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex, ba2int, int2ba
from sympy import randprime, isprime
from random import randint
import launcher
import pickle
import DSA

#Helpers
def str2ba(m): 
    M = list(map(ord, m))
    b = bitarray()
    for x in M:
        b.extend(int2ba(x,8))
    return(b)

def str2int(m):
    return(ba2int(str2ba(m)))

def txt2int(m):
    res = bitarray()
    for i in m:
        res += str2ba(i)
    return ba2int(res)

def int2txt(n):
    res = int2ba(n)
    while(len(res)%8 !=0):
        res = bitarray('0') + res
    bloques = []
    for i in range(0, len(res), 8):
        bloques.append(chr(ba2int(res[i:i+8])))
    res = ''
    return (res.join(bloques))

def escribirFichero(x):
    try:
        output = open("./claves_Gammal.pkl", 'wb')
        pickle.dump(x,output)
        output.close()
    except:
        print("ERROR: No se ha podido escribir el fichero.")

def leerFichero():
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
    p = 2 * q + 1
    while not isprime(p):
        q = randprime(2**159, 2**160)  
        p = 2 * q + 1
    return p

def generarGenerador(p,q):
    g = 1
    a = b = 1 
    while(a == 1 and b == 1):
        a = pow(g, (p-1)//2, p)
        b = pow(g, (p-1)//q, p)
        if(a==1 or b==1):
            g = g + 1
    return g

def generarParametros():

    q = randprime(2**1023, 2**1024)
    p = generarGrupo(q)
    g = generarGenerador(p,q)

    dicc = {}
    dicc['Grupo'] = p
    dicc['Generador'] = g
    escribirFichero(dicc)

    """
    dicc = leerFichero()
    if 'Primo' in dicc: # si Q ya esta creada, se coge del fichero del gammal
        q = dicc['Primo']
        
    else:
        q = randprime(2**1023, 2**1024)
        
    p = generarGrupo(q)
    g = generarGenerador(p,q)

    dicc = {}
    dicc['Primo'] = q
    dicc['Grupo'] = p
    dicc['Generador'] = g
    
    print(dicc)
    escribirFichero(dicc)
    """

def cifrarMensaje(dest, m):
    dicc = leerFichero()
    
    v = randint(1, 2*64) % dicc['Grupo']
    V = pow(dicc['Generador'],v,dicc['Grupo'])
    x = pow(dicc[dest][1],v,dicc['Grupo'])
    c = (str2int(m) * x)
    return (V,c)

def descifrarMensaje(usuario, V, c):
    dicc = leerFichero()
    #print("¿Que usuario eres?")
    #dest = eleccionUsuarios(dicc)
    #V = input("Introduce V: ")
    #c = input("Introduce c: ")
    y = pow(int(V),dicc[usuario][0],dicc['Grupo'])
    m = int(c) // y
    return int2txt(m)



