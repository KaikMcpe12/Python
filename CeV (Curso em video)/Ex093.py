dados = dict()
gols = list()
dados['Nome'] = input('Nome do jogador: ')
qtd = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for i in range (0,qtd):
    gols.append(int(input(f'    Quantos gols na partida {i+1}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print(30*'=')
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(30*'=')
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas')
for k,v in enumerate(dados['Gols']):
    print(f'    => Na partida {k}, fez {v} gols')
print(f'Foi um total de {dados["Gols"]}')