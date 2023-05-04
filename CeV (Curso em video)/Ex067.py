while True:
    n = int(input('Digite a tabuada desejada: '))    
    print(25*'=')
    if n < 0:
        print('Numero negativo')
        print('Terminado...')
        break
    for c in range(1,11):
        print(n,' × ',c,' = ',n*c)
    print(25*'=')