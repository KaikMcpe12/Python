import os
from unidecode import unidecode
from random import *
cores = {'Nulo' : '\033[m','Vermelho' : '\033[31m','Verde' : '\033[32m','Amarelo' : '\033[33m','Azul' : '\033[34m','Roxo' : '\033[35m','Ciano' : '\033[36m','Cinza' : '\033[37m','Branco' : '\033[7;30m'}
boneco = ['____\n|   |\n|\n|\n|\n|','____\n|   |\n|   O\n|\n|\n|','____\n|   |\n|   O\n|   |\n|\n|','____\n|   |\n|   O\n|  /|\n|\n|','____\n|   |\n|   O\n|  /|\\\n|\n|','____\n|   |\n|   O\n|  /|\\\n|  /\n|','____\n|   |\n|   O\n|  /|\\\n|  / \\\n|']

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
    try:
        os.system('CLS')
    except:
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
    
def game_screen(letter,tentativas,secret_str):
    clear()
    título('Jogo da Forca','Vermelho')
    print('\033[33mLetras digitadas:\033[m')
    print(' - '.join(letter))
    linha()
    print(boneco[tentativas],end = ' '*7)
    print(' '.join(secret_str))
    linha()
    
def LerArq(arq):
    try:
        n = open(arq,'rt')
    except:
        print('\033[31mERRO ao abrir o arquivo\033[m')
    else:
        str_list = list(n)
        t = len(str_list)-1
        number = randint(0,t)
        secret_word = str_list[number].strip()
        n.close()
        return secret_word.lower()
        
def start_str(secret_word):
    return ['-' for c in secret_word]
    
def input_letter():
    n = input('Digite a letra: ').strip()
    n = unidecode(n.lower())
    return n
        
def verifica_letter(str,secret_str,secret_word):
    for letter in str:
        for pos,word in enumerate(secret_word):
            if letter == unidecode(word):
                secret_str[pos] = secret_word[pos]
                    
def final_game_screen(letter,tentativas,secret_word,cor):
    clear()
    título('Jogo da Forca','Vermelho')
    print('\033[33mLetras digitadas:\033[m')
    print(' - '.join(letter))
    linha()
    print(f'{cores[cor]}{boneco[tentativas]}{cores["Nulo"]}',end = ' '*7)
    print(f'{cores[cor]}{secret_word}{cores["Nulo"]}')
    linha()