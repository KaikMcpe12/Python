list = []
while True:
    list.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N]').upper()
    if resp in 'N':
        break
print(30*'=')
print(f'Lista: {list}')
print(f'Você digitou {len(list)} números')
list.sort(reverse=True)
print(f'O valores em ordem decrescente: {list}')
if 5 in list:
    print('O 5 está contido na lista')
else:
    print('O 5 não está contido na lista')