n = []
pares = []
ímpares = []
while True:
    n.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(30*'=')
print(f'Lista: {n}')
for c in n:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {ímpares}')