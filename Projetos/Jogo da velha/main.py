from Recursos import *
from Visual import *
from random import randint

num_player = randint(0,1)
resp = home()

if resp == 1:
    linha(30)
    instruções()
    while True:
        pergunta = input('Deseja continuar? [S/N] ').strip()[0]
        if pergunta in 'Ss':
            resp = 2
            break   

while resp == 2:
    começar()
    while True:
        clear()
        título('Jogo da velha','Vermelho')
        mostra_jogador()
        mostra_board()
        linha(30)
        jogador(num_player)
        linha(30)
        posição('Digite a posição: ',num_player)
        if Ganhador(num_player):
            Winner_board()
            break
        num_player = mudaJogador(num_player)
    while True:
        linha(30)
        pergunta = input('Deseja continuar? [S/N] ').strip()[0]
        if pergunta in 'Ss':
            num_player = mudaJogador(num_player)
            limpar_board()
            resp = 2
            break
        elif pergunta in 'Nn':
            resp = 0
            break

clear()
título('Até mais, Volte sempre','Vermelho')