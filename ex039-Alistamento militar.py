from datetime import date

print("""Informe seu sexo:
         1 - Feminino
         2 - Masculino """)

sexo = int(input())

if sexo == 2:

    dataNascimento = int(input("Informe o seu ano de nascimento: "))

    anoAtual = date.today().year

    idade = anoAtual - dataNascimento 

    if idade < 18 :
        print("Ainda irá se alistar! Falta {} ano(s) para se alistar".format(18 - idade))
        print("Voce devera se alistar em ", (anoAtual + (18 - idade)))
    elif idade == 18:
        print("Hora de se alistar!")
    else:
        print("Já passou da hora de se alistar.Passou {} ano(s) da epoca do alistamento".format(idade - 18))
        print("Voce deveria ter se alistar em ", (anoAtual - (idade - 18)))
else:
    print("Você não precisa se alistar")

#para descobrir o ano em que deve se alistar é so pegar o ano atual + a quantidade de anos que falta, se quiser saber quanto passou é so tirar.

