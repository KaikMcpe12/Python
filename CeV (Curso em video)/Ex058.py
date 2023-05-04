from random import randint
print(5*'=','Jogo da adivinhação',5*'=')
print('\033[32mEscolhas: \033[34m0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10\033[m')
number = randint(1,10)
print(20*'-')
n = 0
while n != number:
    n = int(input('Digite um número: '))
    if n == number:
        print('Você acertou o número, parabéns!!!')
    elif n != number:
        print('Você errou, tente novamente')