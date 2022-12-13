from random import randint
import sha1, gammal, DSA

p = 0
alpha = 0
lista = []
user = -1
q = 0
def mostrarMenu():
        print("\n------------------------------------------")
        if(user == -1):
            print("***** Usuario Anonimo *****")
        else:
            print("***** Usuario "+str(user+1)+" *****")
        print("1.- Generar hash SHA-1")
        print("2.- Generar Claves")
        print("3.- Iniciar Sesion")
        print("4.- Firmar un mensaje con clave privada")
        print("5.- Verificar Integridad de Una Firma")
        print("6.- Enviar Mensaje a un Usuario")
        print("7.- Recibir Mensaje de un usuario")
        print("0.- Salir")
        print("------------------------------------------")
        opt = int(input("Introduce una opcion (1-6):\n"))
        return opt

def eleccionUsuario(x):
    print("Seleccione un usuario de los siguientes: ")
    for i in range(len(lista)):
        if(i != x):
            print(str(i+1)+") Usuario "+str(i+1))
    user = input("--> ")
    return int(user)-1

def enviarMensaje():
    print("¿A que usuario va dirigido el mensaje?")
    dest = eleccionUsuario(user)
    m = input("Introduzca el mensaje: \n")

    v = randint(1, 2*64) % p
    V = pow(alpha,v,p)
    x = pow(lista[dest][1],v,p)
    c = (gammal.str2int(m) * x)
    #Emvia (V,c)
    print("m: "+str(gammal.str2int(m)))
    print("Mensaje cifrado: "+str(c))
    y = pow(V,lista[dest][0],p)
    x = c // y
    print("Mensaje descifrado: "+str(x))
    print("Mensaje descifrado en texto: "+gammal.int2txt(x))

if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1:#Generar Hash
            print("Opcion1")
            cad = input("Introduce una cadena:\n")
            print("SHA-1: "+sha1.SHA1(cad)+"\n")
        
        elif(opcion == 2):#Generar claves
            p, alpha, q, lista = gammal.establecerClaves()
            print("\nClaves generadas correctamente.")
        
        elif(opcion == 3):#Iniciar sesion
            if(p == 0):
                print("\nDebe generar primero las claves.")
            else:
                user = eleccionUsuario(user)
                print("Usuario "+str(user+1))
        
        elif(opcion == 4):#Firmar
            if(user == -1):
                print("\nDebe iniciar sesion antes.")
            else:
                x = lista[user][0]
                m = input("Introduce el mensaje a firmar\n")
                r,s = DSA.firma(alpha,m,x,p,q)
                print("r: "+str(r))    
                print("s: "+str(s)) 
        
        elif(opcion == 5):#Verificar firma
            if(user == -1):
                print("\nDebe iniciar sesion antes.")
            else:
                print("¿Que usuario ha firmado el mensaje?")
                dest = eleccionUsuario(-1)
                r = input("Introduce r\n")
                s = input("Introduce s\n")
                m = input("Introduce el mensaje\n")
                y = lista[dest][1]
                print(y)
                res = DSA.verificarFirma(r, s, m, y, p, q, alpha)
                if res:
                    print("La firma es válida\n")
                else:
                    print("La firma *NO* es válida o ha sido comprometida\n")
        
        elif(opcion == 6):#Enviar mensaje
            if(user == -1):
                print("\nDebe iniciar sesion antes.")
            else:
                enviarMensaje()
        
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")
        
