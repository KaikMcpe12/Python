def ficha(j = '<Desconhecido>',g = 0):
    return f'O jogador {j} fez {g} gol(s) no campeonato'
print(30*'=')
jog = input('Nome do jogador: ')
gol = input('Número de Gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    print(ficha(g = gol))
else:
    print(ficha(jog,gol))