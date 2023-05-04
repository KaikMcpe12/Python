number = (int(input('Digite o 1° valor: ')),
int(input('Digite o 2° valor: ')),
int(input('Digite o 3° valor: ')),
int(input('Digite o 4° valor: ')))
print(20*'=')
print(f'Você digitou os número: {number}')
print(f'O número 9 apareceu {number.count(9)} vezes')
if 3 in number:
    print(f'O valor 3 apareceu na posição {number.index(3)+1}°')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados são: ',end=' ')
for n in number:
    if n % 2 == 0:
        print(n,end=' - ')
print('FIM')