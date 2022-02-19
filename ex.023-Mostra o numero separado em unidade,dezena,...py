##informe um número


##mostre na tela os digtos separados.


num = str(input('Digite um número de 0 a 9999: ')).zfill(4)

print('\nO número digitado foi: {}'.format(num))
print('Sua unidade é: {}'.format(num[3]))
print('Sua dezena é: {}'.format(num[2]))
print('Sua centena é: {}'.format(num[1]))
print('seu milhar é: {}'.format(num[0]))

##fazer como numero - int

numero = int(input('Digite um número de 0 a 9999: '))

unidade = numero // 1 % 10 ## retorna o resto da divisão
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('\nO número digitado foi: ',numero)
print('Sua unidade é: ',unidade)
print('Sua dezena é:',dezena)
print('Sua centena é:',centena)
print('Sua milhar é:',milhar)