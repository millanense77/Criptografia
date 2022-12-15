from random import randint
import gammal, DSA

def mainGeneradorParam(tipo):
    #leer Q del fichero
    if (tipo == 'DSA'):
        DSA.generarParametros()
    if(tipo == 'gammal'):
        gammal.generarParametros()
      
def mainGeneradorClaves(tipo):
     if (tipo == 'DSA'):
        altaUsuario('DSA') 
     if(tipo == 'gammal'):
        altaUsuario('gammal')
        
        
#Usuarios
def generarClavePrivada(p):
    return randint(2,p-1)

def generarClavePublica(g,k,p):
    return pow(g,k,p)

def altaUsuario(tipo, nombre):
    if tipo == 'DSA':
        dicc = DSA.leerFichero()
        try:
            k = generarClavePrivada(dicc['Primo'])
            K = generarClavePublica(dicc['Generador'], k, dicc['Grupo'])
            dicc[nombre] = [k, K]
            print(dicc)
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

    