print(20*'=')
print(f"{'Loja baratão':^20}")
print(20*'=')
barato = ' '
gasto = maiores = cont = 0
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: '))
    gasto += preço
    if preço > 1000:
        maiores += 1
    if cont == 0 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break
    cont += 1
print(f"{'FIM do programa':-^40}")
print(f'Total da compra: R${gasto}')
print(f'Produtos maiores de R$1.000: {maiores}')
print(f'Produto mais barato: {barato} -> R${menor}')