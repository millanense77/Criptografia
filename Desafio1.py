from string import ascii_uppercase

alfa = ascii_uppercase

#mensaje = "LS WYVEPTV JBYZV ZL PTWSHUAHU SVZ NYHKVZ KLS WYVJLZV KL IVSVUPH"

def descifrar(mensaje, clave):
    descifrado = ''
    k = alfa.index(clave)
    for letra in mensaje:
        if(letra != ' '):
            pos = alfa.index(letra)
            nueva = (pos - k) % 26
            cifra = alfa[nueva]
            descifrado = descifrado + cifra
        else:
            descifrado += ' '
    print("Clave: " + clave + " " + descifrado)

print("\nIntroduzca el mensaje a descifrar:")
mens=input()
print("\nMensaje: ",mens)

for letra in alfa:
    descifrar(mens, letra)