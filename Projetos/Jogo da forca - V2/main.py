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
    secret_word = LerArq(arq)
    secret_str = start_str(secret_word)
    tentativas = 0
    letter = []
    while True:
        game_screen(letter,tentativas,secret_str)
        str = input_letter()
        letter.append(str)
        if str in unidecode(secret_word):
            verifica_letter(str,secret_str,secret_word)
        else:
            tentativas += 1
        if ''.join(secret_str) == secret_word:
            final_game_screen(letter,tentativas,secret_word,'Verde')
            break            
        elif tentativas == 6:
            final_game_screen(letter,tentativas,secret_word,'Vermelho')
            break