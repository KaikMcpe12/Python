branco = ' '
board = [[branco,branco,branco],[branco,branco,branco],[branco,branco,branco]]
locate = {1 : [0,0],2 : [0,1],3 : [0,2],4 : [1,0],5 : [1,1],6 : [1,2],7 : [2,0],8 : [2,1],9 : [2,2]}
stamp = ['X','O']
players = [0,0]

def limpar_board():
    global board
    board = [[branco,branco,branco],[branco,branco,branco],[branco,branco,branco]]
    
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


def mostra_jogador():
    print(f'\033[33m{f"Jogador X: {players[0]}":<20}\033[32m{f"Jogador O: {players[1]}"}\033[m\n')


def jogador(p):
    print(f'\033[36mJogador:\033[m {stamp[p]}')
    
def mostra_board():
    for i,c in enumerate(board):
        print(' | '.join(c))
        if i < 2:
            print('---------')

def mudaJogador(p):
    if p == 0:
        return 1
    else:
        return 0

def posição(msg,p):
    while True:
        pos = Verifica_Num(msg,9)
        n = locate[pos]
        if board[n[0]] [n[1]] == branco:
            break
        print('\033[31mNão pode ser jogado nessa casa, digite novamente: \033[m')
    board[n[0]][n[1]] = stamp[p]

def Winner_row(p):
    for c in range(0,3):
        if board[c][0] == board[c][1] == board[c][2] and board[c][0] != branco:
            board[c][0] = board[c][1] = board[c][2] = f'\033[32m{stamp[p]}\033[m'
            return True

def Winner_column(p):
    for c in range(0,3):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] != branco:
            board[0][c] = board[1][c] = board[2][c] = f'\033[32m{stamp[p]}\033[m'
            return True

def Winner_diagonal(p):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != branco:
        board[0][0] = board[1][1] = board[2][2] = f'\033[32m{stamp[p]}\033[m'
        return True
    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != branco:
        board[2][0] = board[1][1] = board[0][2] = f'\033[32m{stamp[p]}\033[m'
        return True

def tie():
    for c in board:
        for i in c:
            if i == branco:
                return False
    return True

def Ganhador(p):
    if Winner_row(p) or Winner_column(p) or Winner_diagonal(p):
        print(f'\033[32mWINNER Player {p+1}:\033[m {stamp[p]}')
        players[p] += 1
        return True
    elif tie():
        print('\033[31mTIE, nenhum player ganhou\033[m')
        return True