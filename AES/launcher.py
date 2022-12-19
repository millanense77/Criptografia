import AES_cifrado, AES_descifrado
from bitarray import bitarray
from bitarray.util import ba2hex, int2ba

def mostrarMenu():
    """
    Este metodo muestra el menu principal y permite
    al usuario elegir la opcion.
    No recibe ningun parametro.
    Devuelve un numero entero.
    """
    print("\n------------------------------------------")
    print("1.- Cifrado con CBC")
    print("2.- Descifrar con CBC")
    print("3.- Cifrar con ECB")
    print("4.- Descifrar con ECB")
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-4):\n"))
    return opt

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

def stringToHexadecimal(m):
    """
    Este metodo convierte un string en un numero hexadecimal.
    Recibe una cadena de texto.
    Devuelve un numero hexadecimal.
    """
    try: 
        int(m, 16)
        return m
    except:
        return(ba2hex(str2ba(m)))


if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if(opcion == 0):
            print("Saliendo...")
        else:
            if(opcion == 1):#Cifrado CBC
                msj = input("Introduzca un mensaje: \n")
                key = input("Introduzca una clave: \n")

                IV = stringToHexadecimal(input('Introduzca un vector de inicialización de 16 bytes: '))
                print('\nMensaje sin cifrar: '+str(msj))
                print("Clave: "+str(key))

                CBC = AES_cifrado.CBC_cifrado(stringToHexadecimal(msj), stringToHexadecimal(key), IV)
                print('\nCifrado con CBC: '+str(CBC))
        
            elif(opcion == 2):#Descifrado CBC
                msj = input("Introduzca un mensaje: \n")
                key = input("Introduzca una clave: \n")
                IV = stringToHexadecimal(input('Introduzca un vector de inicialización de 16 bytes: '))
                print('\nMensaje sin descifrar: '+str(msj))
                print("Clave: "+str(key))

                CBC = AES_descifrado.CBC_descifrado(stringToHexadecimal(msj),stringToHexadecimal(key), IV)
                print('\nDescifrado con CBC: '+str(CBC))
            
            elif(opcion == 3):#Cifrado ECB
                msj = stringToHexadecimal(input("Introduzca un mensaje: \n"))
                key = stringToHexadecimal(input("Introduzca una clave: \n"))

                print('\nMensaje sin cifrar: '+str(msj))
                print("Clave: "+str(key))
                ECB = AES_cifrado.ECB_cifrado(msj, key)
                print('\nCifrado con ECB: '+str(ECB))
            
            elif(opcion == 4):#Descifrado ECB
                msj = input("Introduzca un mensaje: \n")
                key = input("Introduzca una clave: \n")

                print('\nMensaje sin cifrar: '+str(msj))
                print("Clave: "+str(key))
                ECB = AES_descifrado.invECB(stringToHexadecimal(msj),stringToHexadecimal(key))
                print('\nDescifrado con ECB: '+str(ECB))

            else:
                print("Opción no válida")
        
