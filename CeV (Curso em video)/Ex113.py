def LeiaInt(msg):
    while True:
        try:
            number = int(input(msg))
        except (TypeError,ValueError):
            print('\033[31mERRO! Digite um número válido\033[m')
        except InteruptError:
            print('\033[31mERRO! O usuário preferiu não digitar\033[m')
            return 0
        else:
            return number

def LeiaFloat(msg):
    while True:
        try:
            number = float(input(msg))
        except (TypeError,ValueError):
            print('\033[31mERRO! Digite um número válido\033[m')
        except InteruptError:
            print('\033[31mERRO! O usuário preferiu não digitar\033[m')
            return 0
        else:
            return number
    
n_int = LeiaInt('Digite um inteiro: ')
n_real = LeiaFloat('Digite um real: ')
print(f'O número inteiro digitado foi {n_int} e o real foi {n_real}')