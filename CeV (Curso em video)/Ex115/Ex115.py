from time import sleep
from lib.interface import *
from lib.arquivo import *


arq = 'Lista.txt'
if not ArqExiste(arq):
    CriaArq(arq)

while True:
    n = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if n == 1:
        LerArq(arq)
    elif n == 2:
        título('NOVO CADASTO')
        nome = input('Nome: ')
        idade = LeiaInt('Idade: ')
        Cadastrar(arq,nome,idade)
    elif n == 3:
        título('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERROR! Digite uma opção válida\033[m')
    sleep(2)