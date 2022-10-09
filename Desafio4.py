cadena = "WUBEFIQLZURMVOFEHMYMWTIXCGTMPIFKRZUPMVOIRQMMWOZMPULMBNYVQQQMVMVJLEYMHFEFNZPSDLPPSDLPEVQMWCXYMDAVQEEFIQCAYTQOWCXYMWMSEMEFCFWYEYQETRLIQYCGMTWCWFBSMYFPLRXTQYEEXMRULUKSGWFPTLRQAERLUVPMVYQYCXTWFQLMTELSFJPQEHMOZCIWCIWFPZSLMAEZIQVLQMZVPPXAWCSMZMORVGVVQSZETRLQZPBJAZVQIYXEWWOICCGDWHQMMVOWSGNTJPFPPAYBIYBJUTWRLQKLLLMDPYVACDCFQNZPIFPPKSDVPTIDGXMQQVEBMQALKEZMGCVKUZKIZBZLIUAMMVZ"

from string import ascii_uppercase as alfabeto
from math import log2 as lg

"""
-----------------------
CALCULO DE LA ENTROPIA
-----------------------
"""
lista = {}
for i in alfabeto:
    lista[i] = cadena.count(i)

H = 0
for j in alfabeto:
    if(lista[j]!=0):
        #Calculamos la probabilidad de que salga la letra en la cadena
        frec = lista[j] / len(cadena)
        #Calculamos la entropia
        H = H + (frec * lg(1/frec))

print("\nH: "+str(H)+"\n")

English = [781, 128, 293, 411, 1305, 288, 139, 585, 677, 23, 42, 360, 262, 728, 821, 215, 14, 664, 646, 902, 277, 100, 149,30, 151, 9]
English = list(map(lambda x: x/10000, English))

cadenas = []
for i in range (5):
    cadenas.append(cadenas[i::5])

for k in range(5):
    
    frecuencias = []
    for letra in alfabeto:
        frecuencias.append(cadenas[k].count(letra))
    
    N = len(cadena[k])
    frecuencias =list(map(lambda x: x/N, frecuencias)) 

    
    listaCC = []

    for j in range(26):
        CC = 0
        for i in range (26):
            CC += frecuencias[i] * English[i]
            
        listaCC.append(CC)
        aux = frecuencias[0]
        del(frecuencias[0])
        frecuencias.append(aux)
    clave=""
    maximo = max(listaCC)
    indice = listaCC.index(maximo)
    clave += alfabeto[indice]
    
    print(clave)

    def resta(letra1,letra2):
        i = alfabeto.index(letra1)
        j = alfabeto.index(letra2)
        k = (i - j) % 26
        return(alfabeto[k])

    L = len(cadena)    
    
    CLAVE = clave * ceil(L/5)
    descifrado = ""

    
    for i in range(L):
        descifrado += resta(cadena[i],CLAVE[i])
    
    print(descifrado)
