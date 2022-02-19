#leia uma velocidade de um carro e mostre se foi multado ou não

velo = float(input("Informe a velocidade atual do carro:"))

valorMulta = (velo - 80 ) * 7

if velo > 80:
    print("Você foi multado.O valor da multa é de : R$ ",valorMulta)
else:
    print("Bom dia, dirija com segurança")

#usar condição simples também, e calcular a multa dentro da condição