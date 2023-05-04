pessoa = []
dados = []
maior = menor = 0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(30*'=')
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi {maior}Kg. De',end=' ')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')     
print(f'\nO menor peso foi {menor}Kg. De',end=' ')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]',end = ' ')