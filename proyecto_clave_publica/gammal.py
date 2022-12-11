from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex, ba2int, int2ba
from sympy import randprime, isprime
from random import randint
import pickle

p = 0
alpha = 0
a = 0
A = 0
b = 0
B = 0

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

def diccionario(p, alpha, E, R, e, r):
    lista = {}
    lista['Grupo'] = p
    lista['Generador'] = alpha
    lista['Emisor_Publica'] = E
    lista['Receptor_Publica'] = R
    lista['Emisor_Privada'] = e
    lista['Receptor_Privada'] = r
    return lista

def escribirFichero(x):  
    #with open('claves.pkl', 'wb') as pickle_out:
     #   pickle.dump(x, pickle_out) # guardamos la lista en un fichero binario
    
    output = open('claves.pkl', 'wb')
    pickle.dump(x,output)
    output.close()
    print('\nFichero generado')

def leerFichero():    
    #with open('claves.pkl', 'rb') as pickle_in:
     #   lectura = pickle.load(pickle_in) # importamos la lista del fichero 
    f=open('claves.pkl','rb')
    lectura=pickle.load(f)
    f.close()

    return lectura

def generarGrupo(q):
    p = 2 * q + 1
    while not isprime(p):
        q = randprime(1, 2**64)
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

def generarNuevasClaves():
    q = randprime(1, 2**64)
    p = generarGrupo(q)
    alpha = generarGenerador(p,q)

    a = randint(2,p-1) #clave privada de A
    A = pow(alpha, a, p) #clave publica de A
    b = randint(2,p-1) #clave privada de A
    B = pow(alpha, b, p) #clave publica de A
    dicc = {}
    dicc = diccionario(p,alpha,A,B,a,b)
    print(dicc)
    escribirFichero(dicc)

def establecerClaves():
    global p 
    global alpha 
    global A 
    global B 
    global a
    global b 
    flag = False

    while(flag == False):
        x = input('¿Desea generar nuevas claves?(Y/n)')
        if(x == 'Y' or x == 'y'):
            flag = True
            generarNuevasClaves()
        if(x == 'n' or x == 'N'):
            flag = True
        if(flag == False):
            print('Introduzca Y, y, N o n')

    dicc = {}
    dicc = leerFichero()
    p = dicc['Grupo']
    alpha = dicc['Generador']
    A = dicc['Emisor_Publica']
    B = ['Receptor_Publica']
    a = dicc['Emisor_Privada']
    b = dicc['Receptor_Privada']
"""
def main():
    establecerClaves()
    print('p: '+str(p))

main()
#x = txt2int('hola')
#y = int2txt(x)
#print('X = '+str(x))
#print('Y = '+str(y))

"""