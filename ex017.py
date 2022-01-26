# o valor da hipotenusa é igual x² = a² + b² onde x é a hipotenusa e a e b são os catetos.
import math
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = math.sqrt((cat_oposto ** 2)+(cat_adjacente ** 2))
# ou
hipotenusa = math.hipot(cat_oposto,cat_adjacente)

print('O valor da hipotenusa é de {:.2f}'. format(hipotenusa))

#ou

cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = ((cat_oposto ** 2)+(cat_adjacente ** 2)) **(1/2)

print('O valor da hipotenusa é de {:.2f}'. format(hipotenusa))

# ou assim 

from math import hypot
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hipot(cat_oposto,cat_adjacente)