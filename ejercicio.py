alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mensaje = 'LS WYVEPTV JBYZV ZL PTWSHUAHU SVZ NYHKVZ KLS WYVJLZV KL IVSVUPH'
clave = 'J'
k = alfa.index(clave)
cifrado = ''

for letra in mensaje:
    pos = alfa.index(letra)
    nueva = (pos + k) % 26
    cifra = alfa[nueva]
    cifrado = cifrado + cifra

print(cifrado)
