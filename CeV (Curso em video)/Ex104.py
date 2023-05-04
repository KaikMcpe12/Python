def Leiaint(msg):
    number = input(msg)
    while not number.isnumeric():
         print('\033[31mERRO! Digite um número inteiro válido\033[m')
         number = input(msg)
    number = int(number)
    return number
n = Leiaint('Digite um número: ')
print(f'Voce acabou de digitar o número: {n}')