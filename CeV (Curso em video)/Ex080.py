n = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > n[-1]:
        n.append(valor)
        print('Valor adicionado na última posição')
    else:
       for i,c in enumerate(n):
           if valor <= c:
               n.insert(i,valor)
               print(f'Valor adicionado na posição {i}')
               break
print(30*'=')
print(f'Números: {n}')