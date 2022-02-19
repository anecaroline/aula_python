nome = input("Qual seu nome:")

if nome == "Ane":
   print("Que nome lindo!")
else:
    print("Bom dia",nome)

    #média
nota1 = input()
nota2 = input()

media = (nota1 + nota2)/2

if media >= 6:
    print("Sua média foi boa.Parabéns")
else:
    print("Sua média foi ruim.Estude mais")

#simplificada
print("Parabens" if media >= 6 else "Estude mais")