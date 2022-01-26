#pergunte a quantidade de km percorridos
#quantidade de dias que foi alugado
#preço a pagar
#custo de R$60,00 por dia e R$0,15 por km rodado

Km = float(input('Informe a quilometragem percorrida pelo carro: '))
dias = float(input('Informe a quantidade de dias usados: '))

custo = Km*0.15 + dias*60

print("O custo de {} quilometros, por {} dias é de R$ {:.2f}".format(Km,dias,custo))