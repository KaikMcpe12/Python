def LeiaInt(msg,teste = 0):
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

def título(msg):
    print(40 * '-')
    print(msg.center(40))
    print(40 * '-')
    
def menu(list):
    título('MENU PRINCIPAL')
    for c,i in enumerate(list):
        print(f'\033[33m{c+1}\033[m - \033[34m{i}\033[m')
    print(40*'-')
    resp = LeiaInt('\033[32mSua opção:\033[m ')
    return resp