#leia o nome, idade e sexo de quatro pessoas.


soma_Idades = 0
nome_homem_MaisVelhor = ''
idade_homem_MaisVelhor = -1 #idade náo pode ser negativa
idade_MulheresMenoresDe20 = 0

for contador in range (1,5):
    nome = str (input("Informe o nome da {} ª pessoa: " . format(contador)))
    idade = int (input("Informe a idade da {}ª pessoa: " . format(contador)))
    sexo = str (input("Informe o sexo da {}ª pessoa. M/F: " . format(contador))).upper()

    soma_Idades += idade

    if sexo == "M":
        if idade  > idade_homem_MaisVelhor :
           idade_homem_MaisVelhor = idade
           nome_homem_MaisVelhor = nome
    else:#mulher
        if idade < 20:
           idade_MulheresMenoresDe20 += 1 


media_Idade = soma_Idades / 4
print("A média de idades desse grupo é: ",media_Idade)
print("A idade do homem mais velho é {} e o nome é {} ".format(idade_homem_MaisVelhor,nome_homem_MaisVelhor))
print("A quantidade de mulher com idade menor que 20 anos é de {} ".format(idade_MulheresMenoresDe20))