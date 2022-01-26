#leia altura e largura em metros, calcule a area e quantidade de tinta pra pintar.
#1 litro de tinta pinta 2 metros quadrados

largura = float(input("Informe a largura da parede:"))
altura = float(input("Informe a altura da parede:"))

#area = largura * altura
#litros = area / 2

print("A área da parede é de {} m² , para pinta-la será necessario {} litros de tinta"
      . format(largura*altura,(largura*altura)/2))