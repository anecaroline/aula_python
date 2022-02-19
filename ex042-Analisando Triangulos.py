a = float(input("Informe o comprimento da retaA:"))
b = float(input("Informe o comprimento da retaB:"))
c = float(input("Informe o comprimento da retaC:"))

#checar se essas retas formam um triangulo
#uma condição é que a soma de dois lados seja maior que o terceiro lado

if a + b > c and a + c > a and a + c > b:
    print("É possivel formar um triangulo")
    #afirmativa é subentendido, diferente da negação que tem que checar todas as opções.
    if a == b and a == c:
        print('O triangulo possue 3 lados iguais, portanto é EQUILATERO')
    elif a != b and a != c and b != c:
        print('O triangulo possue 3 lados diferentes, portanto é ESCALENO')
    else:
        print('O triangulo possue 2 lados iguais e um diferente, portanto é ISOCELES')
else:
    print("Não é possivel formar um triangulo")


