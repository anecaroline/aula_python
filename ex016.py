import math

numero = float(input("Informe um número para arredondamento: "))

print('O numero {} tem a parte inteira {}'.format(numero,math.trunc(numero)))

#ou

from math import trunc

numero = float(input("Informe um número para arredondamento: "))

print('O numero {} tem a parte inteira {}'.format(numero,trunc(numero)))

#ou
numero = float(input("Informe um número para arredondamento: "))
print('O numero {} tem a parte inteira {}'.format(numero,int(numero)))