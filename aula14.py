#contando de 1 a 9.
for contador in range (1,10):
    print(contador,end = " ")
print("Fim")

contador = 1

while contador < 10:
    print(contador,end = " ")
    contador += 1 
print("FIM")

#repetir o input até que seja digitado zero. Não pode usar o for, usa-se o While

numero = 1
resposta = "S"

while numero != 0: #flag condição de parada
    numero = int(input("Informe um número: "))
    reposta = str(input("Quer continuar S/N : ")).upper()
print("fim")


numero = 1
par = 0
impar = 0

while numero != 0: #flag condição de parada
    numero = int(input("Informe um número: "))
    if numero != 0: #tirei o 0 pois ele é uma parada.
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print("fim")
print("Numero pares : ",par )
print("Numero impares : ",impar )
