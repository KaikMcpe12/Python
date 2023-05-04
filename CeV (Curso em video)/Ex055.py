print(5*'=','Pesos',5*'=')
maior = 0
menor = 0
for n in range(1,6):
    peso = int(input(f'Digite o peso da {n}° pessoa: '))
    if n==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(20*'=')
print(f'Maior pesso: {maior}')
print(f'Menor pesso: {menor}')