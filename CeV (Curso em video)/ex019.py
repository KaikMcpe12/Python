import random
print(5*'=','Aluno aleatória',5*'=')
print()
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
print()
print(f'O aluno escolhido foi {random.choice(lista)}')