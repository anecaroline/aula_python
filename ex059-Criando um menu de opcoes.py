#leia dois valores e mostre o menu, e faca a operacao escolhida

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
from enum import Enum

class Menu(Enum):
    Somar = 1
    Multiplicar = 2
    Maior = 3
    Novos_Numeros = 4
    Sair_Programa = 5


numero1 = float(input("Informe o primeiro número:"))
numero2 = float(input("Informe o segundo número:"))

opcao = 0

while opcao != Menu.Sair_Programa:
    print(10*"*******")
    print (""" MENU DE OPÇOES
               1 SOMAR
               2 MULTIPLICAR
               3 MAIOR
               4 NOVOS NÚMEROS
               5 SAIR DO PROGRAMA """)
    print(10*"*******")

    opcao = Menu(int(input("Informe a sua opcao de acordo com o menu acima:")))

    if opcao == Menu.Somar:
        resultado = numero1 + numero2
        print("A soma entre {} + {} é {}".format(numero1,numero2,resultado))
        #break
    elif opcao == Menu.Multiplicar:
       resultado = numero1 * numero2
       print("A multiplicacao entre {} x {} é {}".format(numero1,numero2,resultado))
       #break
    elif opcao == Menu.Maior:
        if numero1 > numero2:
            resultado = numero1
        else:
            resultado = numero2
        print("O maior número entre {} e {} é {}".format(numero1,numero2,resultado))
        #break
    elif opcao == Menu.Novos_Numeros:
        numeroNovo1 = float(input("Informe o primeiro número novo:"))
        numeroNovo2 = float(input("Informe o segundo número novo:"))
    else:    
        #break
        print("Saindo do programa")


