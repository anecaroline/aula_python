#leia 7 datas de nascimento
from datetime import date

anoAtaul = date.today().year

pessoas_MaiorIdade = 0
pessoas_MenorIdade = 0

for pessoa in range (1,8): #1,8 também da 
    nascimento = int (input("Em que ano a {}ª pessoa nasceu : ".format(pessoa)))
    idade = anoAtaul - nascimento
    if idade < 18 :
        pessoas_MenorIdade += 1
    else:
        pessoas_MaiorIdade +=1

print("A quantidade de pessoas com maior idade é de {} ". format(pessoas_MaiorIdade))
print("A quantidade de pessoas com menor idade é de {} ". format(pessoas_MenorIdade))

