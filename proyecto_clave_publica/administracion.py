import gammal, DSA

def mostrarMenu():
    print("1.- DSA generar parametros p,q,g")
    print("2.- ElGamal generar parametros p,g")    
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-2):\n"))
    return opt

if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1: #Generar DSA
            P,N = DSA.eleccionP()
            G = DSA.eleccionG(P, N)
            print(P)
            print(N)
            print(G)
        elif(opcion == 2):#Generar ElGamal
            p,q = gammal.generarGrupo()
            g = gammal.generarGenerador(p, q)
            print(p)
            print(g)
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")