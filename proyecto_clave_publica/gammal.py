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
    output = open("claves_Gammal.pkl", 'wb')
    pickle.dump(x,output)
    output.close()

def leerFichero():
    f=open("claves_Gammal.pkl",'rb')
    lectura=pickle.load(f)
    f.close()
    return lectura


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



def eleccionUsuarios(dicc):
    print("Seleccione un usuario de los siguientes: ")
    for key,value in dicc.items():
        if(key != 'Generador' and key != 'Grupo'):
            print(key)
    user = input("Nombre del usuario: \n")
    return user


def cifrarMensaje():
    dicc = leerFichero()
    print("¿A que usuario va dirigido el mensaje?")
    dest = eleccionUsuarios(dicc)
    m = input("Introduzca el mensaje: \n")

    v = randint(1, 2*64) % dicc['Grupo']
    V = pow(dicc['Generador'],v,dicc['Grupo'])
    x = pow(dicc[dest][1],v,dicc['Grupo'])
    c = (str2int(m) * x)
    print('V: '+str(V))
    print('c: '+str(c))
    #return (V,c)

def descifrarMensaje():
    dicc = leerFichero()
    print("¿Que usuario eres?")
    dest = eleccionUsuarios(dicc)
    V = input("Introduce V: ")
    c = input("Introduce c: ")
    y = pow(int(V),dicc[dest][0],dicc['Grupo'])
    print('y: '+str(y))
    m = int(c) // y
    print(m)
    #return int2txt(m)



