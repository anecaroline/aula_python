##Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
from enum import Enum

class condiçãoPagamentoEnum (Enum):
    dinheiroCheque = 1
    cartaoaVista = 2
    cartaoaVistaDividido = 3
    cartaoaVistaDivididoMais = 4

valorProduto = float(input("Informe o valor do produto em R$ :"))

print(""" As condições de pagamento são:
          1 - A vista dinheiro/cheque (10% de desconto)
          2 - A vista cartão (5% de desconto)
          3 - em até 2x no cartão : preço normal
          4 - 3x ou mais no cartão: 20% de juros""")

condiçãoPagamento = condiçãoPagamentoEnum(int(input("Informe a sua opção de pagamento de acordo com a tabela acima:")))
##acrescentar, pedir o numero de parcelas para a opção 3 e 4. Acrescentar. No if dele
##usar um print apenas, fora do laço pra imprimir tudo sem parcelamento
#crie opção invalida, + um elif

parcelas = 1

if (condiçãoPagamento == condiçãoPagamentoEnum.cartaoaVistaDivididoMais or
    condiçãoPagamento == condiçãoPagamentoEnum.cartaoaVistaDividido):
   parcelas = int(input("Informe a quantidade de parcelas : "))

desconto = 0
juros = 0

if condiçãoPagamento == condiçãoPagamentoEnum.dinheiroCheque:
   desconto = (valorProduto * (10/100))
elif condiçãoPagamento == condiçãoPagamentoEnum.cartaoaVista:
   desconto = (valorProduto * (5/100))
else: # if condiçãoPagamento == condiçãoPagamentoEnum.cartaoaVistaDivididoMais:
   juros = (valorProduto * (20/100))

valorPagar = valorProduto - desconto + juros;

print("O valor do produto eh de R${}".format(valorProduto))
if desconto > 0: print("O valor do desconto eh de R${}".format(desconto))
if juros > 0: print("O valor do juro eh de R${}".format(juros))
print("O valor a pagar eh de R${}".format(valorPagar))

if (parcelas > 1): print("O valor será dividido em {} parcelas de R${.:2f} ".format(parcelas,valorBruto/parcelas))
