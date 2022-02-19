distancia = float(input("Digite a distancia em KM:"))

if distancia <= 200:
    valorPassagem = distancia * 0.50
else:
    valorPassagem = distancia * 0.45
print("O valor da passagem será de : R${} pois a distancia é de {} km ".format(valorPassagem,distancia))