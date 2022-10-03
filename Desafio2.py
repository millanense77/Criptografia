#cifrado = "TYERTSHPIOEITOLTTOHURARSNROTHSCEITYRSNRFHUEIGTOATPIOETI"
cifrado = input('Mensaje cifrado: ')

L = len(cifrado)
k = 2
q = L//k
r = L % k

L = []
inicio = 0
for i in range(r):
    L.append(cifrado[inicio:inicio+q+1])
    inicio += q+1
for i in range(k-r):
    L.append(cifrado[inicio:inicio+q])
    inicio += q
mensaje = ''
for i in range(q):    
    for j in range(k):
        mensaje += L[j][i]
for i in range(r):
    mensaje += L[i][-1]

print(mensaje)