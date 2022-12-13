from bitarray import bitarray
from bitarray.util import hex2ba, ba2hex, ba2int, int2ba
from sympy import randprime, isprime
from random import randint
import pickle
import DSA

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

def lista2Diccionario(lista):
    dicc = {}
    dicc['Grupo'] = lista[0]
    dicc['Generador'] = lista[1]
    dicc['Q'] = lista[2]
    for i in range(3,len(lista)):
        x = "Usuario_"+ str(i-1)
        dicc[x+"_privada"] = lista[i][0]
        dicc[x+"_publica"] = lista[i][1]
    return dicc

def dicc2Lista(dicc):
    lista = []
    aux = []
    for key,value in dicc.items(): 
        aux.append(value)
    lista = [aux[0], aux[1], aux[2]]
    for i in range(3,len(aux)-1,2):
        L = []
        L.append(aux[i])
        L.append(aux[i+1])
        lista.append(L)
    return lista

def escribirFichero(x):
    output = open('claves.pkl', 'wb')
    pickle.dump(x,output)
    output.close()

def leerFichero():
    f=open('claves.pkl','rb')
    lectura=pickle.load(f)
    f.close()
    return lectura

def generarGrupo():
    q = randprime(2**159, 2**160)  
    p = 2 * q + 1
    while not isprime(p):
        q = randprime(2**159, 2**160)  
        p = 2 * q + 1
    return p,q

def generarGenerador(p,q): 
    g = 1
    a = b = 1 
    while(a == 1 and b == 1):
        a = pow(g, (p-1)//2, p)
        b = pow(g, (p-1)//q, p)
        if(a==1 or b==1):
            g = g + 1
    return g

def generarNuevasClaves(nUsuarios):
    q = randprime(2**159, 2**160)  
    p,n = DSA.eleccionP(q)
    alpha = generarGenerador(p,q) #alfa realmente es g
    #alpha = DSA.eleccionG(p,n)
    lista = [p,alpha,q]
    for i in range(nUsuarios):
        L = []
        x = randint(2,p-1)
        X = pow(alpha, x, p) 
        L.append(x)
        L.append(X)
        lista.append(L)
    
    dicc = {}
    dicc = lista2Diccionario(lista)
    escribirFichero(dicc)

def establecerClaves():
    flag = False

    while(flag == False):
        x = input('¿Desea generar nuevas claves?(Y/n): ')
        if(x == 'Y' or x == 'y'):
            flag = True
            i = input('\nIntroduzca cantidad de usuarios: ')
            generarNuevasClaves(int(i))
        if(x == 'n' or x == 'N'):
            flag = True
        if(flag == False):
            print('Introduzca Y, y, N o n')

    dicc = {}
    dicc = leerFichero()
    L = dicc2Lista(dicc)
    return (L[0], L[1], L[2], L[3:])
