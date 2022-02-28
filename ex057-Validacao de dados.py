#leia o sexo da pessoa
#aceita só M ou F
#caso não seja digitado isso, peça pra digitar novamente até que atenda a condição



sexo = str(input("Digite o seu sexo: ")).upper()
  
while sexo != "M" and sexo != "F":
        sexo = str(input("Digite o seu sexo: ")).upper()
print(sexo)   

#segunda forma
sexo = str(input("Digite o seu sexo: ")).upper()

while sexo not in "FfMm": #uso de tratamento com lista de strings
    sexo = str(input("Digite o seu sexo com uma opção válida: ")).upper()
print(sexo)
    