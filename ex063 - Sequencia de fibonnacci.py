#soma do ultimo e penultimo número
#0 , 1 
#0+1 = 1 + 1 = 2 + 3 = 5
#numero_digitado = int(input("Informe um número inteiro para a sequencia de Fibonacci:"))

#penultimo_termo = 0
#ultimo_termo = 1

#while penultimo_termo <= numero_digitado:
#    print(penultimo_termo)
#    proximo_termo = penultimo_termo + ultimo_termo
#    penultimo_termo = ultimo_termo
#    ultimo_termo = proximo_termo


quantidade_termos = int (input("Quantos números deseja mostrar: "))

penultimo_termo = 0
ultimo_termo = 1
contador = 1 # se usar por fora imprimindo o penultimp e ultimo fixo pra otimizar ai sim o contador começa com tres 

#print("{} {}".format(penultimo_termo,ultimo_termo),end=" ")
while contador <= quantidade_termos:
    print(penultimo_termo,end=" ") #e o print aqui será do proximo termo sempre.
    proximo_termo = penultimo_termo + ultimo_termo
    penultimo_termo = ultimo_termo
    ultimo_termo = proximo_termo
    contador += 1