valorCasa = float(input("Informe o valor da casa: R$ "))
salarioComprador = float(input("Informe o seu sálario casa: R$"))
parcelamento = int(input("Informe em quantos anos irá pagar:"))

#valor da prestacao
valorParcela = valorCasa / (parcelamento * 12)
porcentagemSalario = salarioComprador * 0.3

if valorParcela > porcentagemSalario :
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado!Parabéns.")
print("Uma casa no valor {} com o pagamento em {} anos, terá uma parcela mensal de {:.2f}, e a porcentagem minima para aprovação seria 30% do sálario que é {.:2f}"
      .format(valorCasa,parcelamento,valorParcela,porcentagemSalario))
