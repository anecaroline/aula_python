#leia cinco pesos e mostre o maior e o menor
lista_pesos = []

for numero_pesos in range (1,6):
    pesos = float(input("Informe o peso da {} ª pessoa: ".format(numero_pesos)))
    lista_pesos.append(pesos)
print(max(lista_pesos))
print(min(lista_pesos))

import math

minimo = math.inf # maior numero possivel
maximo = -math.inf  #menor numero possivel

for numero_pesos in range (1,6):
    peso = float(input("Informe o peso da {} ª pessoa: ".format(numero_pesos)))
    if peso > maximo :
        maximo = peso
    if peso < minimo :
        minimo = peso
print("O maior peso é {}".format(maximo))
print("O menor peso é {}".format(minimo))

#começando com 0 você coloca nas duas, se for a primeira vez, assim começa analisar a partir dele.
minimo = 0
maximo = 0

for numero_pesos in range (1,6):
    peso = float(input("Informe o peso da {} ª pessoa: ".format(numero_pesos)))
    if peso == 1:
        maximo = peso
        minimo = peso
    else:
        if peso > maximo :
            maximo = peso
        if peso < minimo :
            minimo = peso
print("O maior peso é {}".format(maximo))
print("O menor peso é {}".format(minimo))