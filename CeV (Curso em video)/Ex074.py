from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(5*'=','Números aleatórios',5*'=')
print('Números:')
for number in n:
        print(number,end = '-')
print(f'\n\nMaior valor: {max(n)}')
print(f'Menor valor: {min(n)}')



#maior = n[0]
#menor = n[0]
#for c in n:
#    if c > maior:
#        maior = c
#    if c < menor:
#        menor = c