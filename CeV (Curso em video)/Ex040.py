nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
media = (nota1 + nota2)/2
if media<5:
    print(f'O aluno está reprovado com média {media}')
elif media>=5 and media<7:
    print(f'O aluno está de recuperação com média {media}')
elif media>=7:
    print(f'O aluno está aprovado com média {media}')