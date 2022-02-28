#leia o primeiro termo e mostre os 10 primeiros dessa progressão (PA)
#PA o proximo número é a razão + o número anterior...

#leia o temos e a razão
termoAnterior = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

#calculo dos 10 termos


for _ in range (10):

    proximoTermo = termoAnterior + razao
    print(proximoTermo)
    termoAnterior = proximoTermo


contador = 0

while contador < 10 :

    proximoTermo = termoAnterior + razao
    print(proximoTermo)
        
    contador += 1
    termoAnterior = proximoTermo

    


#pa para o primeiro termo = 26 e razão = 5, PA = 26,31,36,41,46,51,56,61,66,71,76
#26 + 5 = 31

decimo = termoAnterior + (10 - 1) * razao
for c in range (termoAnterior,decimo + razao ,razao):
    print("{}". format(c),end = ' ->')
print("ACABOU")