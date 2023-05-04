from time import sleep
def contador(início,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(15*'-=')
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if início < fim:
        c = início
        while c <= fim:
            print(c,end = ' > ',flush = True)
            sleep(0.5)
            c += 1
    else:
        c = início
        while c >= fim:
            print(c,end = ' > ',flush = True)
            sleep(0.5)
            c -= 1
    print('END')
    print(15*'-=')
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)