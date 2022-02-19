PrimeiroNumero = int(input("Informe o primeiro número:"))
SegundoNumero = int(input("Informe o segundo número:"))

if PrimeiroNumero == SegundoNumero: ## ou essa condição como else, bem melhor
    print("Não existe maior valor,os dois são iguais")
elif PrimeiroNumero > SegundoNumero:
    print(" O primeiro valor é o maior : ",PrimeiroNumero)
elif SegundoNumero > PrimeiroNumero :
    print(" O segundo valor é o maior: ",SegundoNumero) 

## ou essa condição como else, bem melhor
if PrimeiroNumero > SegundoNumero:
    print(" O primeiro valor é o maior : ",PrimeiroNumero)
elif SegundoNumero > PrimeiroNumero :
    print(" O segundo valor é o maior: ",SegundoNumero) 
else: 
    print("Não existe maior valor,os dois são iguais")


#if PrimeiroNumero == SegundoNumero:
#    print("Não existe maior valor,os dois são iguais")
#else:
#    print(" O primeiro maior valor é: ",max(PrimeiroNumero,SegundoNumero))
#    print(" O segundo maior valor é: ",min(PrimeiroNumero,SegundoNumero))