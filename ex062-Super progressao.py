termo_usuario = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

contador = 0 # variavel de controle sempre o que está na condição do while
termo_atual = termo_usuario
contador_mais = 10
total = 0

while contador_mais != 0 :
    total = contador_mais + total
    while contador <= total :
        
        print(termo_atual, end = " "  )
        proximoTermo = termo_atual + razao
           
        contador += 1
    
        termo_atual = proximoTermo #acumulador , algo que auxilia no calculo e sempre muda com o while, acabando o laço eçe cai fora

    print()
    contador_mais = int(input("Quantos termos você quer mostrar a mais: "))
print("Progressão finalizada com {} termos mostrados".format(total))   

