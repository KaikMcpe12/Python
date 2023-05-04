print(5*'=','Grupo',5*'=')
s = 0
h_velho = 0
Mulher20 = 0
for cont in range(1,5):
    nome = input(f'Nome da {cont}° pessoa: ')
    idade = int(input(f'Idade da {cont}° pessoa: '))
    sexo = input(f'Sexo da {cont}° pessoa [f/m]: ')
    print(20*'-')
    s +=idade
    if sexo.upper()=='M' and idade>h_velho:
        h_velho=idade
        mais_velho = nome
    if idade<20 and sexo.upper=='F':
        Mulher20+=1
print(f'\nMédia das idades: {s/4}')
print(f'Homem mais velho: {mais_velho}')
print(f'Mulheres menores de 20: {Mulher20}')