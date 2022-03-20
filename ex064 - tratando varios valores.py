numero = 0
contador = 0
soma = 0
numero_parada = 999 #flag (condição de parada)

#primeira forma

while numero != numero_parada:
    numero = int(input("Digite um número ou {} para parar: ".format(numero_parada)))
   
    if numero != numero_parada:
        soma += numero
        contador += 1

 #segunda forma

while True:
    numero = int(input("Digite um número ou {} para parar: ".format(numero_parada)))
   
    if numero != numero_parada:
        soma += numero
        contador += 1
    else:
        break

 #terceira forma , mais eficiente

while True:
    numero = int(input("Digite um número ou {} para parar: ".format(numero_parada)))
   
    if numero == numero_parada:
        break
    soma += numero
    contador += 1
    
        
print(soma)
print(contador)


