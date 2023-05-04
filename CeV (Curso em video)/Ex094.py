dados = dict()
grupo = list()
s = 0
while True:
    dados['Nome'] = input('Nome: ')
    while True:
        dados['Sexo'] = input('Sexo [M/F]: ').upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    dados['Idade'] = int(input('Idade: '))
    s += dados['Idade']
    grupo.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp in 'Nn':
        break
print(30*'=')
m = s / len(grupo)
print(f'- O grupo tem {len(grupo)} pessoas')
print(f'- A média de idade é de {m:.2f} anos')
print(f'- As mulheres cadrastadas foram: ',end = '')
for c in grupo:
    if c['Sexo'] in 'Ff':
        print(c['Nome'],end = ' ')
print('\n- A lista das pessoas que estão acima da média: ')
for c in grupo:
    if c['Idade'] >= m:
        print('    ',end='')
        for k,v in c.items():
            print(f'{k} = {v};',end=' ')
        print()
print('\n<< ENCERRADO >>')