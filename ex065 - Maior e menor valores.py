import math

numero = 0
contador = 0
soma = 0
numero_parada = 9999
maximo = - math.inf
minimo = math.inf

while True:
    numero = int(input("Digite um número ou {} para parar: ".format(numero_parada)))
   
    if numero == numero_parada:
        break
    soma += numero
    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero

    contador += 1
media = soma / contador
print(media)
print(maximo)
print(minimo)

## com a resposta de parada pelo usuario sem a flag 9999

numero = 0
contador = 0
soma = 0
parada = "S"
maximo = - math.inf
minimo = math.inf

while parada in "sS":
    numero = int(input("Digite um número: "))
   
    
    soma += numero

    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero

    contador += 1
    parada = str(input("Informe se quer continuar S/N: ")).upper().strip()[0]
media = soma / contador
print(media)
print(maximo)
print(minimo)