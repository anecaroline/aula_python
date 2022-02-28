#multiplos de 3 numeros que sáo divisiveis por 3
#intervalo de 1 a 500

soma = 0
contador = 0

for numeros in range (1,501,2):
    if numeros % 3 == 0 :
        soma  += numeros
        contador += 1


print("A soma de {} valores é de {} " .format(contador,soma))
        
   