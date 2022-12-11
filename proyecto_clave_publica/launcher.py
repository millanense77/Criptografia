import sha1
import gammal
import DSA

def mostrarMenu():
        print("------------------------------------------")
        print("1.- Generar hash SHA-1")
        print("2.- Generar Claves")
        print("3.- Firmar un mensaje con clave privada")
        print("4.- Verificar Integridad de Una Firma")
        print("0.- Salir")
        print("------------------------------------------")
        opt = int(input("Introduce una opcion (1-4):\n"))
        return opt


if __name__ == "__main__":
    opcion = 1
    while(opcion!= 0):
        opcion = int(mostrarMenu())
        if opcion == 1:
            print("opcion1")
            cad = input("Introduce una cadena:\n")            
            print("SHA-1: "+sha1.SHA1(cad))
        elif(opcion == 2):
            gammal.establecerClaves()
            
        elif(opcion == 3):
            g = input("Introduce el generador\n")
            x = input("Introduce la clave privada\n")
            m = input("Introduce el mensaje a firmar\n")
            r,s = DSA.firma(g,m,x)
            print(r,s)
        elif(opcion == 4):
            r = input("Introduce r\n")
            s = input("Introduce s\n")
            m = input("Introduce el mensaje\n")
            y = input("Introduce la clave publica\n")
            res = DSA.verificarFirma(r, s, m, y)
            if res:
                print("La firma es válida\n")
            else:
                print("La firma *NO* es válida o ha sido comprometida\n")
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opción no válida")
        
