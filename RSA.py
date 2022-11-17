from math import gcd
from random import randint
from sympy import randprime

p = randprime(10**99, 10**100)

q = randprime (1**119, 10**120)

n = p * q  # type: ignore

fi = (p-1) * (q-1)  # type: ignore

e = randint(2,fi-1)

gcd (e,fi)

d = pow(e, -1, fi)