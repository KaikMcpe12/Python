from datetime import date
atual = date.today().year
maior = 0
menor = 0
for n in range(1,8):
    nasc = int(input(f'Digite a data de nascimento da {n}° pessoa: '))
    id = atual-nasc
    if id>21:
        maior+=1
    elif id<21:
        menor+=1
print(f'Maiores: {maior}')
print(f'Menores: {menor}')