import sha1, gammal, DSA


def mostrarMenu():
    """
    Este metodo muestra el menu principal y permite
    al usuario elegir la opcion.
    No recibe ningun parametro.
    Devuelve un numero entero.
    """
    print("\n------------------------------------------")
    print("1.- Generar hash SHA-1")
    print("2.- Cifrado mensaje con ElGammal")
    print("3.- Descifrar mensaje con el ElGammal")
    print("4.- Firmar con DSA")
    print("5.- Verificar firma con DSA")
    print("0.- Salir")
    print("------------------------------------------")
    opt = int(input("Introduce una opcion (1-5):\n"))
    return opt

def eleccionUsuarios(tipo):
    """
    Este metodo muestra los usuarios registrados 
    en los ficheros de DSA y/o gammal.
    Recibe una cadena de text que contiene 
    la eleccion del fichero a elegir.
    Devuelve una cadena de texto
    """
    if(tipo == 'DSA'): dicc = DSA.leerFichero()
    else: dicc = gammal.leerFichero()
    flag = False
    lista = dicc.keys()
    
    if((tipo == 'DSA' and len(lista)<=3)
    or (tipo == 'gammal' and len(lista)<=2)):
        print("No hay usuarios registrados en el sistema.")
        return ""
    else:
        while(flag == False):
            print("Seleccione un usuario de los siguientes: ")
            i = 1
            for key in lista:
                if(key != 'Generador' and key != 'Grupo' and key != 'Primo'):
                    print(str(i)+') '+str(key))
                    i += 1
            user = input("Nombre del usuario: \n")
            flag = user in lista
            if(flag == False): print("Nombre no valido, elija uno de la lista.\n")
    return user

if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1:#Generar Hash
            print("Opcion1")
            cad = input("Introduce una cadena:\n")
            print("SHA-1: "+sha1.SHA1(cad)+"\n")
    
        elif(opcion == 2):#Cifrado
            nombre = eleccionUsuarios('gammal')
            if(nombre != ""):
                mensaje = input("\nIntroduzca mensaje a enviar: \n")
                V, c = gammal.cifrarMensaje(nombre, mensaje)
                print('\nV: '+str(V))
                print('c: '+str(c))
        
        elif(opcion == 3):#Descifrado
            usuario = eleccionUsuarios('gammal')
            if(usuario != ""):
                V = input("V: ")
                c = input("c: ")
                m = gammal.descifrarMensaje(usuario, V, c)
                print("\nMensaje descifrado: "+str(m))
        
        elif(opcion == 4):#Firmar
            emisor = eleccionUsuarios('DSA')
            if(emisor != ""):
                m = input("Introduce mensaje a firmar: \n")
                r,s = DSA.firma(emisor, m)
                print('R: '+str(r))
                print('s: '+str(s))

        elif(opcion == 5):#Verificar Firma
            emisor = eleccionUsuarios('DSA')
            if(emisor != ""):
                m = input("Introduce el mensaje\n")
                r = input("Introduce r\n")
                s = input("Introduce s\n")
                res = DSA.verificarFirma(r, s, m, emisor)
                if res:
                    print("\nLa firma es válida\n")
                else:
                    print("\nLa firma *NO* es válida o ha sido comprometida\n")

        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")
        