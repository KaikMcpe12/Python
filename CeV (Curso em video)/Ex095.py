time = list()
while True:
    dados = dict()
    gols = list()
    dados['Nome'] = input('Nome do jogador: ')
    qtd = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for i in range (0,qtd):
        gols.append(int(input(f'    Quantos gols na partida {i+1}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp in 'Nn':
        break
    print(30*'=')
print(20*'-=')
print(f'{"cod":<5}',end = '')
for d in dados.keys():
    print(f'{d:<15}',end = '')
print()
print(40*'-')
for k,v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print(40*'-')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i,c in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {c} gols')
    print(30*'-')
print('<< VOLTE SEMPRE >>')