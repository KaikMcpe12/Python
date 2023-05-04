n = []
for c in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = n[c]
        menor = n[c]
maior = max(n)
menor = min(n)
print(30*'=')
print(f'Você digitou os valores: {n}')
print(f'O maior número digitado foi {maior} nas posições: ',end=' ')
for i,c in enumerate(n):
    if c == maior:
        print(f'{i}...',end='')
print(f'\nO menor número digitado foi {menor} nas posições: ',end=' ')
for i,c in enumerate(n):
    if c == menor:
        print(f'{i}...',end='')