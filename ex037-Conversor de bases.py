##leia um número e questione a base para qual quer converter.

#numero = int(input("informe o número que deseja converter:"))
#print("o numero a ser convertido será ",numero)
#print("""temos 3 opções de conversão de bases
#        1 - para binário
#        2- para octal
#        3- para hexadecimal """)
#numeroconvertido = int(input("informe em qual base deseja converte-lo:"))
##convertendo com funções
#if numeroconvertido == 1:
#    print("o número {} na base binária é {}".format(numero,bin(numero)[2:]))
#elif numeroconvertido == 2:
#    print("o número {} na base octal é {}".format(numero,oct(numero)[2:]))
#elif numeroconvertido == 3:
#    print("o número {} na base hexadecimal é {}".format(numero,hex(numero)[2:]))
#else:
#    print("digite uma opção válida")
#    Utilize chr() para converter um número inteiro em um caractere em Python
#    Utilize ord() para converter um caractere para um Inteiro em Python
#print(chr(ord('a') + 2))

digitos = []

quociente = 63
base = 16

while quociente > 0 :
    
    resto = quociente % base 
   
    #print(resto)
    if resto < 10:
        digitos.append(str(resto))
    else:
        digitos.append(chr(ord('a') + resto - 10))
                            
    quociente = quociente // base

digitos.reverse()
print("".join(digitos))
