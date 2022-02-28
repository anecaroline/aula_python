#leia um número inteiro e mostre se é ou não primo
#números primos aqueles que são divisiveis somente por 1 ou por ele mesmo.

numeroVerificar = int(input("Informe o número para verificar se é primo: "))


# maior primo 618970019642690137449562111

divisor = 2
eh_primo = True
metade_numero = numeroVerificar / 2

#se for 1,2 ele pula o while pq já eh primo
while divisor <= metade_numero  or not eh_primo:
    #se o resto da divisão do numero inserido pelo usuario por numero ( inicia com 2) der zero não é primo
    if numeroVerificar % divisor == 0:
        eh_primo = False
        #break
    
    divisor += 1

eh_primo = True
metade_numero = numeroVerificar // 2

if numeroVerificar % 2 == 0:
    eh_primo = False
else:
    for divisor in range (3,metade_numero + 1,2):
        if numeroVerificar % divisor == 0:
            eh_primo = False
            break

if eh_primo:
    print("eh primo!")
else:
    print("nao eh primo!")








#excluindo os números pares e impares(multiplos de 2,3,5).

# 1  2  3  4  5  6  7  8  9 10
#11 12 13 14 15 16 17 18 19 20
#21 22 23 24 25 26 27 28 29 30

# 1   3  5  7  9
#11  13 15 17 19
#21  23 25 27 29

# 1  5  7
#11 13 17 19
#23 25 29

# 1  7
#11 13 17 19
#23 29


