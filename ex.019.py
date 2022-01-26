
import random


#print(random.choice(lista_alunos))


aluno1 = input("Informe o nome do primeiro aluno:")
aluno2 = input("Informe o nome do primeiro aluno:")
aluno3 = input("Informe o nome do primeiro aluno:")
aluno4 = input("Informe o nome do primeiro aluno:")

lista_alunos = []
# ou
lista_alunos=[aluno1,aluno2,aluno3]

#ai não usa o append
lista_alunos.append(aluno1)
lista_alunos.append(aluno2)
lista_alunos.append(aluno3)
lista_alunos.append(aluno4)

print(lista_alunos)
print("O aluno escolhido é : " ,random.choice(lista_alunos))

