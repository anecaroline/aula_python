frase = str(input("Digite uma frase:")).strip().upper()
print("A quantidade de letras A na frase é de:", frase.count("A"))
print("A primeira posição da letra A é:",frase.index('A'))
print("A ultima posição da letra A é:",frase.rindex('A'))

#no lugar do index da pra usar o find também.
# o +1 mostra o contador a partir do 1 e não do zero, fica "melhor" pro usuario.
print("A primeira posição da letra A é:",frase.find('A')+1)
print("A ultima posição da letra A é:",frase.rfind('A'))