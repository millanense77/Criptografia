import sha1, gammal, DSA


def mostrarMenu():
        print("\n------------------------------------------")
        print("1.- Generar hash SHA-1")
        print("2.- Iniciar Sesion")
        print("3.- Cifrado mensaje con ElGammal")
        print("4.- Descifrar mensaje con el ElGammal")
        print("5.- Firmar con DSA")
        print("6.- Verificar firma con DSA")
        print("0.- Salir")
        print("------------------------------------------")
        opt = int(input("Introduce una opcion (1-6):\n"))
        return opt

def eleccionUsuarios(tipo):
    if(tipo == 'DSA'): dicc = DSA.leerFichero()
    else: dicc = gammal.leerFichero()

    print("Seleccione un usuario de los siguientes: ")
    i = 1
    for key,value in dicc.items():
        if(key != 'Generador' and key != 'Grupo' and key != 'Primo'):
            print(str(i)+') '+str(key))
            i += 1
    user = input("Nombre del usuario: \n")
    return user

if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1:#Generar Hash
            print("Opcion1")
            cad = input("Introduce una cadena:\n")
            print("SHA-1: "+sha1.SHA1(cad)+"\n")
    
        elif(opcion == 3):#Cifrado
            nombre = eleccionUsuarios('gammal')
            mensaje = input("\nIntroduzca mensaje a enviar: \n")
            V, c = gammal.cifrarMensaje(nombre, mensaje)
            print('V: '+str(V))
            print('c: '+str(c))
        
        elif(opcion == 4):#Descifrado
            usuario = eleccionUsuarios('gammal')
            V = input("V: ")
            c = input("c: ")
            m = gammal.descifrarMensaje(usuario, V, c)
            print("Mensaje descifrado: "+str(m))
        
        elif(opcion == 5):#Firmar
            emisor = eleccionUsuarios('DSA')
            m = input("Introduce mensaje a firmar: \n")
            r,s = DSA.firma(emisor, m)
            print('R: '+str(r))
            print('s: '+str(s))
        elif(opcion == 6):#Verificar Firma
            r = input("Introduce r\n")
            s = input("Introduce s\n")
            m = input("Introduce el mensaje\n")
            emisor = eleccionUsuarios('DSA')
            res = DSA.verificarFirma(r, s, m, emisor)
            if res:
                print("La firma es válida\n")
            else:
                print("La firma *NO* es válida o ha sido comprometida\n")
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")
        
