#conversor de temperatura
#Para converter graus Celsius em graus Fahrenheit, multiplique por 1,8 e adicione 32.
#°F = °C × 1, 8 + 32
#Para converter graus Fahrenheit em graus Celsius, subtraia 32 e divida por 1,8.
#°C = (°F − 32) ÷ 1, 8

celsius = float(input("Informe a temperatura em Graus Celsius:"))

far = celsius * 1.8 + 32

print("A conversão de {} para Fahrenheit é de {} ".format(celsius,far))


