import gammal, DSA

def mostrarMenu():
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
        if opcion == 1: #Generar usuarios DSA
            nombre = int(input("Introduce tu nombre de usuario:\n"))
            P = int(input("Introduce P:\n"))
            Q = int(input("Introduce Q:\n"))
            G = int(input("Introduce G:\n"))
            
        elif(opcion == 2): #Generar usuarios ElGamal
            nombre = int(input("Introduce tu nombre de usuario:\n"))
            p = int(input("Introduce p:\n"))
            g = int(input("Introduce g:\n"))
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")