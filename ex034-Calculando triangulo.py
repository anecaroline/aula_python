#leia o tamanho de 3 retas
a = float(input("Informe o comprimento da retaA:"))
b = float(input("Informe o comprimento da retaB:"))
c = float(input("Informe o comprimento da retaC:"))

#checar se essas retas formam um triangulo
#uma condição é que a soma de dois lados seja maior que o terceiro lado

if a + b > c and a + c > a and a + c > b:
    print("É possivel formar um triangulo")
else:
    print("Não é possivel formar um triangulo")