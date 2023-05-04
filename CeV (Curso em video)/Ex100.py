from time import sleep
from random import randint
números = list()
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0,6):
        n = randint(1,10)
        lista.append(n)
        print(n,end = ' ',flush = True)
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    s_par = 0
    for c in lista:
        if c % 2 == 0:
            s_par += c
    print(f'Somando os valores pares de {lista}, temos {s_par}')
sorteia(números)
somaPar(números)