#leia quanto de dinheiro tem na carteira e quanto pode comprar em dolla. 1 Dollar = 5,46 reais

dinheiro = float(input("Informe quanto você tem na carteira: R$"))

print("Com R$ {} você pode comprar U$ {:.2f} dolares ". format(dinheiro,dinheiro/5.46))
print("Com R$ {} você pode comprar  {:.2f} Euro ". format(dinheiro,dinheiro/6.19))