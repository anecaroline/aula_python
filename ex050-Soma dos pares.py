listaNumeros = []

for _ in range (0,6):
    numero = int(input())
    listaNumeros.append(numero)

soma = 0

for numeros in listaNumeros:
    if numeros % 2 == 0:
        soma += numeros
print("A soma dos números é ",soma)


## outra forma

soma = 0
count = 0

for c in range (1,7):
    num = int(input("Digite o {} valor:".format(c)))
    if num % 2 == 0:
        soma += num
        count += 1 
print("Você informou {} números pares e a soma foi {} ".format (count,soma))
        




