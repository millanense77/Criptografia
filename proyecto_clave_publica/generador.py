from random import randint
import gammal
import DSA


def mainGeneradorParam(tipo):
    #leer Q del fichero
    if (tipo == 'DSA'):
        DSA.generarParametros()
    if(tipo == 'gammal'):
        gammal.generarParametros()
      
def mainGeneradorClaves(tipo,usuario):
     if (tipo == 'DSA'):
        altaUsuario('DSA',usuario) 
     if(tipo == 'gammal'):
        altaUsuario('gammal',usuario)
        
        
#Usuarios
def generarClavePrivada(p):
    return randint(2,p-1)

def generarClavePublica(g,k,p):
    return pow(g,k,p)

def altaUsuario(tipo,usuario):
    if tipo == 'gammal':
        dicc = DSA.leerFichero()
        try:
            q = dicc['Primo']
            p = dicc['Grupo']
            g = dicc['Generador']
            
            k = generarClavePrivada(p)
            K = generarClavePublica(g,k,p)
            dicc[usuario] = [[k], [K]]
            #escribir usuario en el fichero
            print(dicc)
            gammal.escribirFichero(dicc)
        except:
            print("ERROR: No ha sido posible dar de alta al usuario.")
    if tipo == 'DSA':
        dicc = gammal.leerFichero()
        try:
           
            q = dicc['Primo']
            p = dicc['Grupo']
            g = dicc['Generador']
            
            k = generarClavePrivada(q) 
            K = generarClavePublica(g,k,p)
            dicc[usuario] = [[k], [K]]
            #escribir usuario en el fichero
            print(dicc)
            
           
            DSA.escribirFichero(dicc)
        except:
            print("ERROR: No ha sido posible dar de alta al usuario.")

    