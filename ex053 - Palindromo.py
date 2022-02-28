#leia uma frase e informe se é palindromo - frase igual de traz pra frente.

frase = str(input("Informe a frase pra ver se é PALINDROMO: ")).upper().replace(' ','').strip()
#print(frase)

indiceDireita = len(frase)-1
indiceEsquerda = 0
eh_palindromo = True
#print(indiceDireita)
#print(indiceEsquerda)

while  indiceEsquerda < indiceDireita:
    if frase[indiceEsquerda] != frase[indiceDireita]:
        eh_palindromo = False
        break
    indiceDireita -= 1
    indiceEsquerda += 1


if eh_palindromo:
    print("A palavra {} É PALINDROMO".format(frase))
else:
    print("O inverso de {} é {}". format (frase,frase[::-1]))
    print("A palavra {} Não é PALINDROMO".format(frase))


#outra forma é inverter a palavra e comparar
frase = str(input("Informe a frase pra ver se é PALINDROMO: ")).upper().replace(' ','').strip()
fraseInversa = frase[::-1] #slice

print("o INVERSO de {} é {} ".format(frase,fraseInversa))

if frase == fraseInversa:
    print("É palindromo")
else:
    print("Não é palindromo")