
import math

angulo = float(input('Informe o valor do ângulo: '))
angulorad = math.radians(angulo)
print(angulorad)

print('O valor do seno do angulo {} é {}, o cosseno é {:.0f} e a tangente {}'. format(angulo,math.sin(angulorad),math.cos(angulorad),math.tan(angulorad)))

#arredondamento da bo.