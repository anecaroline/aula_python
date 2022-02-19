numero1 = float(input("Informe o primeiro número:"))
numero2 = float(input("Informe o segundo número:"))
numero3 = float(input("Informe o terceiro número:"))

print(max(numero1,numero2,numero3))
print(min(numero1,numero2,numero3))

#com if
#considera um primeiro valor como sendo o menor
menor = a
if b<a and b<c:
	menor = b
if c<a and c<b:
	menor = c

maior = a
if b>a and b>c:
	maior = b
if c>a and c>b:
	maior = c
print("O menor valor digitado foi {}". format(menor))
print("O maior valor digitado foi {}". format(maior))