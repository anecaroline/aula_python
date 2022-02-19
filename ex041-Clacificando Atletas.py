from datetime import date

anoNascimento = int(input("Informe o ano do seu nascimento: "))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

print("Sua idade é de ", idade ,"anos")

if idade <= 9 :
	print("Sua categoria é MIRIM")
elif idade <= 14:
	print("Sua categoria é INFANTIL")
elif idade <= 19:
	print("Sua categoria é JUNIOR")
elif idade <= 25:
	print("Sua categoria é SÊNIOR")
else:
	print("Sua categoria é MASTER")
