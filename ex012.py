#preço com 5% de desconto

produto = float(input('Informa o valor do produto R$ : '))

print("Seu novo valor com 5% de desconto é de R$:", produto -(produto* (5/100)))

#salario com 15% de aumento
salario = float(input("Informe o seu o valor do seu sálario: R$"))

salarioatual = salario + (salario *(15/100))

print("O seu salario com aumento será de R$", salarioatual)

#valor do produto com preço a vista (desconto de 10%) e a prazo (8% de aumento)
produto = float(input('Informa o valor do produto R$ : '))

avista= produto - (produto * (10/100))
prazo = produto + (produto * (8/100))

print("O valor do produto é de R${}, a vista sai por {:.2f} com 10% de desconto e a prazo sai por R$ {:.2f} com 8% de acrescimo"
      . format(produto,avista,prazo))
