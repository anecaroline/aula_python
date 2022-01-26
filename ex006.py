## mostre o seu dobro,triplo e raiz quadrada.

numero = int(input("Digite um número:"))

print("O dobro do número {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}"
      .format(numero,numero*2,numero*3, numero **(1/2)))
print("O dobro do número {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}"
      .format(numero,numero*2,numero*3, pow(numero,(1/2)))