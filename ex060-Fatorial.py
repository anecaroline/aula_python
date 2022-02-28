#fatorial
#5! = 5 x 4 x 3 x 2 x 1 = 120
#a multiplicação de n por todos os seus antecessores até chegar em 1. n! = n · (n – 1)· (n – 2) · … 
#somente numeros naturais (inteiros positivos)
#0! = 1
#1! = 1

#de frente a ordem dos tratores náo afetam o produto.
ate_numero = int(input("Digite um número: "))
fatorial = 1
fat_numero = 1

while fat_numero <= ate_numero:
    fatorial *= fat_numero 
    fat_numero += 1
    
print(fatorial)
#de tras pra frente
numero = int(input("Fatorial de: ") )
contador = numero
fatorial = 1

print("Calculando {}! = ".format(numero,end = " "))
while contador > 0:
    print("{}".format(contador,end = " "))
    print(" x " if contador > 1 else "=",end = " ")
    fatorial *= contador
    contador -= 1
print("{}".format(fatorial))

#com o for
numero = int(input("Fatorial de: ") )

fatorial=1

for contador in range(1,numero+1):
    fatorial *= contador

print(fatorial)

#biblioteca fatorial
from math import factorial

numero = int(input("Fatorial de: ") )
fatorial = factorial(numero)
print(fatorial)
