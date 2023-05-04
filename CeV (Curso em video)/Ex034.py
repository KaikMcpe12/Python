RS = float(input('Digite seu salário: '))
if RS > 1250:
    aumento = 0.1*RS
    print(f'Com aumento de R${aumento} (10%) seu salário ficará R${RS+aumento}')
else:
    aumento = 0.15*RS
    print(f'Com o aumento de R${aumento} (15%) seu salário ficará R${RS+aumento}')