import os
from Recursos import *
from time import sleep

cores = {'Nulo' : '\033[m','Vermelho' : '\033[31m','Verde' : '\033[32m','Amarelo' : '\033[33m','Azul' : '\033[34m','Roxo' : '\033[35m','Ciano' : '\033[36m','Cinza' : '\033[37m','Branco' : '\033[7;30m'}

def título(msg,cor = 'Nulo',tam = 12):
    t = len(msg) + tam
    print(cores[cor],end = '')
    print(t * '=')
    print(f'{msg:^{t}}')
    print(t * '=')
    print(cores['Nulo'],end = '')
    
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

    
def home():
    título('Jogo da velha','Vermelho')
    print('Escolha:')
    print(f'\033[32m{"Instruções [1]":<20}\033[33mJogar [2]\033[m\n')
    resp = Verifica_Num('\033[7m=>\033[m ',2)
    return resp

def mostra_intruções():
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    for c in board:
        print(' | '.join(c))
        print('----------')

def instruções():
    print('Essas são as posições de cada casa:')
    mostra_intruções()
    print('Cada jogador será nomeado por O ou X')
    print('Vence o jogador que conseguir marcar a sua respetiva figura 3 vezes em uma linha, coluna ou diagonal')
    print(30*'=')

def linha(n,stamp = '='):
    print(n*stamp)
 
def começar():
    linha(30)
    print('Começando em...')
    for t in range(3,0,-1):
        print(t,end = '... ',flush = True)
        sleep(1)   
        
def Winner_board():
    clear()
    título('Jogo da velha','Vermelho')
    mostra_jogador()
    mostra_board()