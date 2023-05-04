import os
import unidecode
from random import *
secret_str = list()
letras = list()
cores = {'Nulo' : '\033[m','Vermelho' : '\033[31m','Verde' : '\033[32m','Amarelo' : '\033[33m','Azul' : '\033[34m','Roxo' : '\033[35m','Ciano' : '\033[36m','Cinza' : '\033[37m','Branco' : '\033[7;30m'}
boneco = ['____\n|   |\n|\n|\n|\n|','____\n|   |\n|   O\n|\n|\n|','____\n|   |\n|   O\n|   |\n|\n|','____\n|   |\n|   O\n|  /|\n|\n|','____\n|   |\n|   O\n|  /|\\\n|\n|','____\n|   |\n|   O\n|  /|\\\n|  /\n|','____\n|   |\n|   O\n|  /|\\\n|  / \\\n|']
tentativa = 0

def título(msg,cor = 'Nulo',tam = 12):
    t = len(msg) + tam
    print(cores[cor],end = '')
    print(t * '=')
    print(f'{msg:^{t}}')
    print(t * '=')
    print(cores['Nulo'],end = '')
    
def Verifica_Num(msg,param):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mERRO! Digite novamente\033[m')
        else:
            if 0 < n <= param:
                return n
            else:
                print('\033[31mERRO! Digite novamente\033[m')
                
def home():
    título('Jogo da forca','Vermelho')
    print('Escolha:')
    print(f'\033[32m{"Instruções [1]":<20}\033[33mJogar [2]\033[m\n')
    
def dificuldade():
    clear()
    título('Jogo da forca','Vermelho')
    print('Escolha a dificuldade:')
    print(f'\033[32m{"Nível 1 [1]":<20}\033[35mNível 4 [4]')
    print(f'\033[33m{"Nível 2 [2]":<20}\033[36mNível 5 [5]')
    print(f'\033[34mNível 3 [3]\033[m\n')
      
def clear():
    os.system('clear')
        
def linha(tam = 30):
    print('='*tam)
    
def instruções():
    print('\033[34mA palavra será sorteada automaticamente')
    print('Você digitará apenas uma letra por vez (Caso seja digitado mais de uma letras, será descontando nas tentativas, a menos que seja a palavra certa)\033[m')
    linha(20)
    print('Você tem 6 chances de acertar a palavra')
    linha(20)
    print('\033[33mCaso já saiba a palavra pode escreve-la por completo e será automaticamente corrigida')
    print('Mas caso erre, perderá uma chance\033[m')
    linha(20)
    print('Visual do boneco caso perca:')
    print('____\n|   |\n|   O\n|  /|\\\n|  / \\\n|')
    linha(20)
    
def game_screen():
    clear()
    título('Jogo da Forca','Vermelho')
    print('\033[33mLetras digitadas:\033[m')
    if len(letras):
        print(' - '.join(letras))
    linha()
    print(boneco[tentativa],end = ' '*7)
    secret_print()
    linha()
    
def LerArq(arq):
    global secret_word
    global copy_secret_word
    try:
        n = open(arq,'rt')
    except:
        print('\033[31mERRO ao abrir o arquivo\033[m')
    else:
        str_list = list(n)
        t = len(str_list)-1
        number = randint(0,t)
        secret_word = str_list[number].replace('\n','')
        copy_secret_word = unidecode.unidecode(secret_word.lower())
        secret()
    finally:
        n.close()
        
def secret():
    for p in secret_word:
        if p == ' ' or p == '-':
            secret_str.append(p)
        else:
            secret_str.append('-')
            
def secret_print():
    for c in secret_str:
        print(c,end = '')
    print()
    
def verifica_word(str):
    if unidecode.unidecode(str.lower()) == unidecode.unidecode(secret_word.lower()):
        return True
    else:
        return False
        
def verifica_letter(str):
    global copy_secret_word
    global secret_str
    str = unidecode.unidecode(str.lower())
    if str in copy_secret_word:
        while str in copy_secret_word:
            n = copy_secret_word.find(str)
            secret_str[n] = secret_word[n]
            copy_secret_word = copy_secret_word.replace(str,' ',1)
    else:
        del_tentativa()
 
def del_tentativa():
    global tentativa
    tentativa += 1
                                            
def append_letter(str):
    letras.append(str)
    
def winner():
    if ''.join(secret_str) == secret_word:
        return True
    else:
        return False
        
def loser():
    if tentativa == 6:
        return True
    else:
        return False
                    
def final_game_screen(cor):
    clear()
    título('Jogo da Forca','Vermelho')
    print('\033[33mLetras digitadas:\033[m')
    print(' - '.join(letras))
    linha()
    print(f'{cores[cor]}{boneco[tentativa]}{cores["Nulo"]}',end = ' '*7)
    print(f'{cores[cor]}{secret_word}{cores["Nulo"]}')
    linha()