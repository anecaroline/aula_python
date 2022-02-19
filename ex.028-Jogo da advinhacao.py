#gerar numeros aleatorios de 0 a 5

import random

numeroComputador = random.randint(0,5)

numeroUsuario = int(input("Informe o número que você acha que o computador escolheu entre 0 a 5 :"))

if numeroUsuario == numeroComputador :
    print("Você ganhou!")
    
else:
    print("Você perdeu!O numero escolhido pelo computador foi:",numeroComputador)
