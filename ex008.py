medida = float(input("Digite um número em metros:"))

dm = medida * 10
cent = medida * 100
mil = medida * 1000
dam = medida / 10
hm = medida /100
km = medida / 1000

print("A conversão de {} para centimetro é {} , para milimetros é {} e dicemetros é {}".format(medida,cent,mil,dm))
print("A conversão de {} para decametros é {} ,para hectometros é {} e quilometros é {}".format(medida,dam,hm,km))
