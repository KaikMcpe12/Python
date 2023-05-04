from random import randint
cont = 0
print(25*'=')
print('Par ou ímpar')
print(25*'=')
while True:
    par = impar = False
    j = int(input('Digite um valor: '))
    esc = input('Você que par ou ímpar [P/I]? ').upper()
    pc = randint(1,10)
    s = j + pc
    print(25*'=')
    print(f'Você jogou {j} e o computador {pc}. Total de {s}',end=' ')
    if s % 2 == 0:
        par = True
        print('Deu PAR')
    else:
        impar = True
        print('Deu ÍMPAR')
    print(25*'=')
    if esc == 'P' and impar or esc == 'I' and par:
       #a variável ímpar ou par é uma booleana, então dependendo do valor a condição será executada
       print('Você perdeu')
       break 
    print('Você ganhou!!!')
    cont += 1
    print(15*'-=')
print(15*'-=')
print(f'GAME OVER! Você venceu {cont} vezes')