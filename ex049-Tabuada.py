#tabuada com um número dado pelo usuario
base = int(input("Informe um valor para ser calculada a tabuada: "))
multiplicador = 0

for multiplicador in range (0,11):
    resultado = base * multiplicador
    print("{} X {} = {} ".format (base,multiplicador,resultado))





for base in range (0,11):

     multiplicador = 0

     while multiplicador <= 10:
        resultado = base * multiplicador
        
        print("{} X {} = {} ".format (base,multiplicador,resultado))   
        multiplicador += 1  


print()

#funcionou, o que muda por ultimo deve vir primeiro, o laço será completado dentro e após fora.
for base in range (0,11):
    for multiplicador in range (0,11):
        resultado = base * multiplicador
        print("{} X {} = {} ".format (base,multiplicador,resultado)) 

#funcionou, incrementar o multiplicador mas quando chegar no 11 voltar ele pra zero,pra começar tudo novamente.
base = 0

while base <= 10:
    
    multiplicador = 0
    
    while multiplicador <= 10:
        resultado = base * multiplicador
        print("{} X {} = {} ".format (base,multiplicador,resultado))   
        multiplicador += 1 
    base += 1