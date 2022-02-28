import random
#geracao de numeros aleatorios
numeroComputador = random.randint(0,10)
#print(numeroComputador)
numeroUsuario = int(input("Informe o número que você acha que o computador escolheu entre 0 a 10 :"))
numeroTentativas = 1

while numeroUsuario != numeroComputador:
    numeroUsuario = int(input("Você errou,o computador escolheu o número {} e você o número {}.Informe o número que você acha que o computador escolheu entre 0 a 10 : ".format(numeroComputador,numeroUsuario)))
    numeroTentativas += 1
    if numeroUsuario < numeroComputador:
        print("Mais.. Tente novamente!")
    elif numeroUsuario > numeroComputador: 
        print("Menos.. Tente novamente!")
print("Você acertou,mas foram {} tentativas para descobrir o número que o computador pensou.".format(numeroTentativas))

#segunda forma 
acertou = False
numeroTentativas = 1

while not acertou:
    numeroUsuario = int(input("Informe o número que você acha que o computador escolheu entre 0 a 10 :"))
    numeroTentativas = 1
    if numeroUsuario == numeroComputador:
        acertou = True
    else:
        if numeroUsuario < numeroComputador:
            print("Mais.. Tente novamente!")
        elif numeroUsuario > numeroComputador:
            print("Menos.. Tente novamente!")
print("Acertou com {} tentativas.Parabéns".format(numeroTentativas))
