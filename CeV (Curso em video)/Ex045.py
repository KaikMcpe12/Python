from random import randint
from time import sleep
print(5*'=','Jokenpô',5*'=')
print('''\033[31m[0]\033[m - Pedra
\033[32m[1]\033[m - Papel
\033[33m[2]\033[m - Tesoura''')
PC = randint(0,2)
print(20*'=')
jg = int(input('Digite a sua jogada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print(20*'=')
if PC==0:
    print('Computador jogou Pedra')
    if jg==0:
        print('EMPATE!!')
    elif jg==1:
        print('VENCEU!!')
    elif jg==2:
         print('PERDEU!!')
elif PC==1:
    print('Computador jogou Papel')
    if jg==0:
        print('PERDEU!!')
    elif jg==1:
        print('EMPATE!!')
    elif jg==2:
        print('VENCEU!!')
elif PC==2:
    print('Computador jogou Tesoura')
    if jg==0:
        print('VENCEU!!')
    elif jg==1:
        print('PERDEU!!')
    elif jg==3:
        print('EMPATE!!')