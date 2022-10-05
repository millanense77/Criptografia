from bitarray import bitarray

IRRED = bitarray('100011011')

def xtime(b):
    if b[0] == 0:
        b.append(0)
        del(b[0])
    else:
        b.append(0)
        b = b ^ IRRED
        del(b[0])
    return(b)

def ident (b):
    return(b)

def mult03(b):
    return(xtime(b) ^ b)