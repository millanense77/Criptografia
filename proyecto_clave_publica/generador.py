from random import randint
import gammal, DSA

def mainGeneradorParam(tipo):
    """
    Este metodo crea los parametros para el algoritmo
    que se le indique, ElGamal o DSA.
    Recibe una cadena de texto.
    Devuelve un boolenao.
    """
    if (tipo == 'DSA'):
        return DSA.generarParametros()
    if(tipo == 'gammal'):
        return gammal.generarParametros()
      
def mainGeneradorClaves(tipo):
    """
    Este metodo da de alta a un usuario empleando
    los parametros del algoritmo recibido.
    Recibe una cadena de texto.
    No devuelve nada.
    """
    if (tipo == 'DSA'):
        altaUsuario('DSA') 
    if(tipo == 'gammal'):
        altaUsuario('gammal')
        
        
#Usuarios
def generarClavePrivada(p):
    """
    Este metodo crea la clave privada de un usuario,
    generando un numero entero aleatorio.
    Recibe un numero entero.
    Devuelve un numero entero.
    """
    return randint(2,p-1)

def generarClavePublica(g,k,p):
    """
    Este metodo crea la clave publica de un usuario,
    calculando el generador(numero entero) elevado a la clave
    privada modulo el grupo finito.
    Recibe tres numero enteros.
    Devuelve un numero entero.
    """
    return pow(g,k,p)

def altaUsuario(tipo, nombre):
    """
    Este metodo da de alta a un usuario con su nombre 
    empleando los parametros del algortimo recibido.
    Recibe dos cadenas de texto.
    No devuelve nada.
    """
    if tipo == 'DSA':
        dicc = DSA.leerFichero()
        try:
            k = generarClavePrivada(dicc['Primo'])
            K = generarClavePublica(dicc['Generador'], k, dicc['Grupo'])
            dicc[nombre] = [k, K]
            DSA.escribirFichero(dicc)
        except:
            print("ERROR: No ha sido posible dar de alta al usuario.")
    if tipo == 'gammal':
        dicc = gammal.leerFichero()
        try:
            k = generarClavePrivada(dicc['Grupo'])
            K = generarClavePublica(dicc['Generador'], k, dicc['Grupo'])
            dicc[nombre] = [k, K]
            gammal.escribirFichero(dicc)
        except:
            print("ERROR: No ha sido posible dar de alta al usuario.")
