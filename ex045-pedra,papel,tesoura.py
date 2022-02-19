 #Crie um programa que faça o computador jogar Jokenpô com você.
 #opções - pedra,papel e tesoura.
 #regras: papel ganha da pedra(embrulha ela),a tesoura ganha do papel (corta),e a pedra ganha da tesoura porque corta.
import random
from enum import Enum

class Peca(Enum):
    Pedra = 1
    Papel = 2
    Tesoura = 3

class Ganhador(Enum):
    Computador = 234
    Usuario = 523523
    Empate = 21342

print("pedra", Peca.Pedra)
print("tisora", Peca.Tesoura)
print("papel", Peca.Papel)

print("Seja Bem-Vindo ao JOGO JOKEMPÔ")
print(6*"*****")
print("""Opções existentes :
         1 - Pedra
         2 - Papel
         3 - Tesoura """)
print(6*"*****")
print("Enquanto voce pensa, eu vou escolhendo a minha.")
escolhaDoComputador = Peca(random.randint(1,3))
print("computa", escolhaDoComputador, repr(escolhaDoComputador), escolhaDoComputador.value)
print(escolhaDoComputador)
print("Muito bem, já pensou ?")
escolhaDoUsuario = Peca(int(input(("Informe a sua escolha:"))))

if escolhaDoComputador == escolhaDoUsuario:
    resultado = Ganhador.Empate
elif escolhaDoComputador == Peca.Pedra:
    if escolhaDoUsuario == Peca.Papel:
        resultado = Ganhador.Usuario
    else:
        resultado = Ganhador.Computador
elif escolhaDoComputador == Peca.Papel:
    if escolhaDoUsuario == Peca.Pedra:
        resultado = Ganhador.Computador
    else:
        resultado = Ganhador.Usuario
else: # comp = tesoura
    if escolhaDoUsuario == Peca.Pedra:
        resultado = Ganhador.Usuario
    else:
        resultado = Ganhador.Computador

if resultado == Ganhador.Empate:
    print("Deu empate!")
elif resultado == Ganhador.Usuario:
    print("Você ganhou!") 
else:
    print("Eu ganhei. Boa sorte na proxima!") 

print("Você escolheu {} e o computador {}".format(escolhaDoUsuario,escolhaDoComputador))

##import time from sleep
#print("JO")
#sleep(1)
#print("KEM")
#sleep(1)
#print("PO")
#sleep(1)