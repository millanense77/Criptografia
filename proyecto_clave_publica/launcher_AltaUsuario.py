import generador

def mostrarMenu():
    """
    Este metodo muestra el menu principal y permite
    al usuario elegir la opcion.
    No recibe ningun parametro.
    Devuelve un numero entero.
    """
    print("1.- Generar claves de usuario DSA")
    print("2.- Generar claves de usuario ElGamal")    
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-2):\n"))
    return opt

if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if(opcion == 0):
            print("Saliendo...")
        else:
            nombre = input("Introduce tu nombre de usuario:\n")
            if opcion == 1: #Generar usuarios DSA
                generador.altaUsuario('DSA', nombre)
                
            elif(opcion == 2): #Generar usuarios ElGamal
                generador.altaUsuario('gammal', nombre)
            else:
                print("Opción no válida")