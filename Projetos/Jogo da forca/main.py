from Recursos import *

home()
resp = Verifica_Num('\033[7m=>\033[m ',2)
linha()

if resp == 1:
    instruções()
    while True:
        pergunta = input('Deseja continuar? [S/N] ').strip()[0]
        if pergunta in 'Ss':
            resp = 2
            break
            
if resp == 2:
    dificuldade()
    resp = Verifica_Num('\033[7m=>\033[m ',5)
    if resp == 1:
        arq = 'Palavras-1.txt'
    elif resp == 2:
        arq = 'Palavras-2.txt'
    elif resp == 3:
        arq = 'Palavras-3.txt'
    elif resp == 4:
        arq = 'Palavras-4.txt'
    else:
        arq = 'Palavras-5.txt'
    LerArq(arq)
    while True:
        game_screen()
        str = input('Digite a letra: ').strip()
        append_letter(str)
        if len(str) == 1:
            verifica_letter(str)
        elif verifica_word(str):
            final_game_screen('Verde')
            break
        else:
            del_tentativa()
        if winner():
            final_game_screen('Verde')
            break            
        elif loser():
            final_game_screen('Vermelho')
            break