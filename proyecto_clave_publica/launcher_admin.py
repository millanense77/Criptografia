import generador

def mostrarMenu():
    print("1.- DSA generar parametros p,q,g")
    print("2.- ElGamal generar parametros p,g")    
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-2):\n"))
    return opt

def crearFichero(name):
    try:
        output = open(name, 'wb')
        output.close()
    except:
        print("ERROR: No se ha podido crear el fichero.")

def gestionFichero(name):
   try:
       file = open(name)
       file.close()
   except FileNotFoundError:
       print('Sorry the file we\'re looking for doesn\'t exist')
       crearFichero(name)

if __name__ == "_main_":
    gestionFichero('claves_DSA.pkl')
    gestionFichero('claves_gammal.pkl')
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1: #Generar DSA
            generador.mainGeneradorParam('DSA')
            print("Claves Generadas correctamente.")
            
        elif(opcion == 2):#Generar ElGamal
            generador.mainGeneradorParam('gammal')
            print("Claves Generadas correctamente.")
           
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")