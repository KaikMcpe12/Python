num = [[], []]
for n in range(1,8):
    valor = int(input(f'Digite o {n}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(30*'=')
num[0].sort()
num[1].sort()
print(f'Números pares: {num[0]}')
print(f'Números ímpares: {num[1]}')