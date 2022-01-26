#ordem de apresentação
import random


aluno1 = input("Informe o nome do primeiro aluno:")
aluno2 = input("Informe o nome do primeiro aluno:")
aluno3 = input("Informe o nome do primeiro aluno:")
aluno4 = input("Informe o nome do primeiro aluno:")

lista_alunos=[aluno1,aluno2,aluno3,aluno4]

#print(random.choices(lista_alunos, k =4))
random.shuffle(lista_alunos)
print("A ordem da lista será: ")
print(lista_alunos)