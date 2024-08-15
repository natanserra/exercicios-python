import random


def sorteio_alunos(lista):
    escolhido = random.choice(lista)
    print(f'O sorteado foi {escolhido}')


aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))

lista = [aluno3, aluno2, aluno1, aluno4]

sorteio_alunos(lista)
