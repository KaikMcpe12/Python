print('''\033[31m[0]\033[m - Dinheiro/Cheque
\033[32m[1]\033[m - Cartão
\033[33m[2]\033[m - 2× no cartão
\033[34m[3]\033[m - 3× ou mais no cartão''')
print(15*'=')
esc = int(input('Digite a forma de pagamento: '))
produto = float(input('Digite o valor do produto: '))
print(15*'=')
if esc==0:
    valor=produto*0.9
    print(f'Dinheiro/cheque: 10% de desconto')
    print(f'Novo valor: R${valor}')
elif esc==1:
    valor=produto*0.95
    print(f'Cartão: 5% de desconto')
    print(f'Novo valor: R${valor}')
elif esc==2:
    print(f'2× no cartão: Preço normal')
    print(f'Novo valor: R${valor}')
elif esc==3:
    valor=produto*1.2
    print(f'3× ou mais no cartão: 20% de juros')
    print(f'Novo valor: R${valor}')