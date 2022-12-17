import generador

def mostrarMenu():
    """
    Este metodo muestra el menu principal y permite
    al usuario elegir la opcion.
    No recibe ningun parametro.
    Devuelve un numero entero.
    """
    print("1.- DSA generar parametros p,q,g")
    print("2.- ElGamal generar parametros p,g")    
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-2):\n"))
    return opt

def crearFichero(name):
    """
    Este metodo crea un fichero con el nombre recibido.
    Recibe una cadena de texto.
    No devuelve nada.
    """
    try:
        output = open(name, 'wb')
        output.close()
    except:
        print("ERROR: No se ha podido crear el fichero.")

def gestionFichero(name):
    """
    Este metodo comprueba si el fichero indicado existe,
    si no existe lo crea.
    Recibe una cadena de texto.
    No devuelve nada.
    """
    try:
        file = open(name)
        file.close()
    except FileNotFoundError:
        print('Sorry the file we\'re looking for doesn\'t exist')
        crearFichero(name)

if __name__ == "__main__":
    gestionFichero('claves_DSA.pkl')
    gestionFichero('claves_gammal.pkl')
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1: #Generar DSA
            flag = generador.mainGeneradorParam('DSA')
            if(flag): print("Claves Generadas correctamente.")
            else: print("No se han podido generar las claves.")
            
        elif(opcion == 2):#Generar ElGamal
            flag = generador.mainGeneradorParam('gammal')
            if(flag): print("Claves Generadas correctamente.")
            else: print("No se han podido generar las claves.")
           
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")