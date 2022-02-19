#para ser bissexto tem que ser divisivel por 4, e se for divisivel por 100 e por 400 também

from datetime import date

ano = int(input('Informe o ano? Coloque 0 para analisar o ano atual:  '))

if ano == 0:
    #pega o ano atual
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))

else:
    print('O ano {} não é um ano bissexto'.format(ano))