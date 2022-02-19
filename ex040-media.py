nota1 = float(input("Infome sua primeira nota:"))
nota2 = float(input("Infome sua segunda nota:"))

media = (nota1 + nota2) / 2

if media < 5:
    print("REPROVADO, sua média foi de :" , media)
elif media > 5 and media < 6.9:
    print("RECUPERAÇÃO, sua média foi de :" , media)
else:
    print("APROVADO, sua média foi de :" , media)
