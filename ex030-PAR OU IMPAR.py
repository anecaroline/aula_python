#leia um numero inteiro e informa se é PAR ou IMPAR

numero = int(input("Informe um número inteiro:"))

if numero % 2 == 0:
    print("O número {} é PAR!".format(numero))
else:
    print("O número {} é IMPAR!".format(numero))