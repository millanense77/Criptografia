from time import time

ini = time()

lista = [3,7,2,9]

print(list(map(lambda x:x**2, lista)))

fin = time()

print(fin - ini, 's') 