termo_usuario = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))


contador = 0 # variavel de controle sempre o que está na condição do while
termo_atual = termo_usuario

while contador < 10 :

    print(termo_atual, end = " ")
    proximoTermo = termo_atual + razao
           
    contador += 1
    
    termo_atual = proximoTermo #acumulador , algo que auxilia no calculo e sempre muda com o while, acabando o laço eçe cai fora
    #ajuda a carregar uma iteração para a proxima

contador = 1
termo = termo_usuario

while contador <= 10:
    print("{} - ".format(termo,end = " "))
    termo += razao
    contador += 1