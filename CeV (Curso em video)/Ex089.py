turma = []
aluno = []
nota = []
while True:
    s = 0
    aluno.append(input('Nome: '))
    nota.append(int(input('Nota 1: ')))
    nota.append(int(input('Nota 2: ')))
    for i in nota:
        s += i
    #s = sum(nota)
    m = s/2
    aluno.append(nota[:])
    aluno.append(m)
    turma.append(aluno[:])
    aluno.clear()
    nota.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break   
print(30*'-')
print(f'{"N°.":<5}{"NOME":<10}{"MÉDIA"}')
print(30*'-')
for c,i in enumerate(turma): 
    print(f'{c:<5}{i[0]:<10}{i[2]:.1f}')
print(30*'-')
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if resp == 999:
        break
    if resp <= len(turma) - 1:
        print(f'Notas de {turma[resp][0]} são {turma[resp][1]}')
    print(30*'-')
print('<<<< VOLTE SEMPRE >>>>')



#turma = []
#while True:
#    aluno = input('Nome: ')
#    nota1 = int(input('Nota 1: '))
#    nota2 = int(input('Nota 2: '))  
#    m = (nota1/nota2)/2
#    turma.append([aluno,[nota1,nota2],m])
#    resp = input('Quer continuar? [S/N] ')
#    if resp in 'Nn':
#        break   
#print(30*'-')
#print(f'{"N°.":<5}{"NOME":<10}{"MÉDIA"}')
#print(30*'-')
#for c,i in enumerate(turma): 
#    print(f'{c:<5}{i[0]:<10}{i[2]:.1f}')
#print(30*'-')
#while True:
#    resp = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
#    if resp == 999:
#        break
#    if resp <= len(turma) - 1:
#        print(f'Notas de {turma[resp][0]} são {turma[resp][1]}')
#    print(30*'-')
#print('<<<< VOLTE SEMPRE >>>>')