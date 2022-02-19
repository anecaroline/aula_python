#leia o salario do funcionario

salario = float(input("Informe seu sálario:"))

#calcular os aumentos
if salario > 1250:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)

print("De acordo com seu salario de R${} seu aumento será para R${}". format(salario,aumento))