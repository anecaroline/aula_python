#leia peso e altura
peso = float(input("Informe o seu peso: (KG)"))
altura = float(input("Informe a sua altura: (M)"))
#informe o IMC
# IMC = PESO/ (ALTURA * ALTURA) OU PESO/(ALTURA)²

IndiceDeMassaCorporal = peso / (altura * altura)

#classificações

if IndiceDeMassaCorporal < 18.5:
    print("Abaixo do peso")
elif IndiceDeMassaCorporal <= 25:
    print("Peso ideal")
elif IndiceDeMassaCorporal <= 30:
    print("Sobrepeso")
elif IndiceDeMassaCorporal <= 40:
    print("Obesidade")
else:
    print("Obesidade Morbida")
print("IMC = {.:2f} ".format(IndiceDeMassaCorporal))

