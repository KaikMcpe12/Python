from time import sleep
cores = {'Nulo' : '\033[m','Vermelho' : '\033[41m','Verde' : '\033[42m','Amarelo' : '\033[43m','Azul' : '\033[44m','Roxo' : '\033[45m','Ciano' : '\033[46m','Cinza' : '\033[47m','Branco' : '\033[7;30m'}
def MostraLinha(msg,cor = 'Nulo'):
    t = len(msg)+4
    print(cores[cor],end = '')
    print(t * f'=')
    print(f'{msg:^{t}}')
    print(t * '=')
    print(cores['Nulo'],end = '')
    sleep(1)
def Ajuda(object):
    MostraLinha(f'Acessando o manual do comando\'{object}\'','Ciano')
    print(cores['Amarelo'],end = '')
    help(object)
    print(cores['Nulo'],end = '')
    sleep(2)
while True:
    MostraLinha('Sistema de ajuda PyHelp','Verde')
    resp = input('Função ou Biblioteca > ')
    if resp.upper() == 'FIM':
        break
    else:
        Ajuda(resp)
MostraLinha('Até Logo','Vermelho')