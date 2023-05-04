import random
print(5*'=','Ordem aleatória de alunos',5*'=')
print()
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print()
print('A ordem de alunos será:')
print(lista)