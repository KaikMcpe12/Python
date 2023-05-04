from  time import sleep
print(30*'=')
def maior (*v):
    cont = maior = 0
    print('Analisando os valores passados...')
    for c in v:
        print(c,end = ' ',flush = True)
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print(30*'=')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()