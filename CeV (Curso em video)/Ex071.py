print(20*'=')
print(f"{'BANCO CEV':^20}")
print(20*'=')
valor = int(input('Digite o saque: R$'))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced != 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 2
        elif ced == 2:
            ced = 1
        if valor == 0:
           break
        totced = 0
print(20*'=')
print('ENCERRANDO...')