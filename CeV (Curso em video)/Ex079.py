n = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in n:
        print('Valor adicionado com sucesso...')
        n.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(30*'=')
n.sort()
print(f'Você digitou os valores: {n}')