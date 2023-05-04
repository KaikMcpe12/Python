from random import randint
from time import sleep 
lista = list()
jogos = list()
print(30*'=')
print(f'{"JOGO DA MEGA SENA":^30}')
print(30*'=')
qtd = int(input('Quantos jogos você quer sortear? '))
for c in range(0,qtd):
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(f'{"SORTEANDO OS NÚMEROS":=^30}')
for i,l in enumerate(jogos):
    print(f'{i+1}° Sorteio - {l}')
    sleep(1)
print(f'{"BOA SORTE":=^30}')