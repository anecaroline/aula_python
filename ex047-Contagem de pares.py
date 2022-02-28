#mostre todos os numeros pares entre 1 e 50

#mais custoso,checa cada numero se é divisivel por 2 pra depois retornar.
for numero in range (1,51):
    if numero % 2 == 0:
        print(numero,end = ' ')

print()

#menos custoso, pega do numero 2 ate o 50 pulando de 2 em 2.Sabemos que o 1 nào é, ja vamos para o 2 e pulando de 2 em 2.
for numero in range (2,51,2):
    print(numero,end = ' ')