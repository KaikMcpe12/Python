aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = int(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5  <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(30*'=')
for k,v in aluno.items():
    print(f'    -{k} é igual a {v}')