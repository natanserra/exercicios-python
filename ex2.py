import random




aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))

lista = [aluno3, aluno2, aluno1, aluno4]
random.shuffle(lista)

print(f'O sorteado foi {lista}')
