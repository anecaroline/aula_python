#conversor de temperatura
#Para converter graus Celsius em graus Fahrenheit, multiplique por 1,8 e adicione 32.
#°F = °C × 1, 8 + 32
#Para converter graus Fahrenheit em graus Celsius, subtraia 32 e divida por 1,8.
#°C = (°F − 32) ÷ 1, 8

far = float(input('Informa a temperatura em Fahrenheit: '))

celsius = (far - 32) / 1.8

print('A temperatura em Fahrenheit de {} é em Celsiu de {}'.format(far,celsius))
