print('\033[31m[1]\033[m - Decimal => Base Qualquer')
print('\033[32m[2]\033[m - Base Qualquer => Decimal')
print(30*'-')
esc1 = int(input('Escolha o número: '))
print(30*'-')
if esc1==1:
    print('\033[31m[1]\033[m - Decimal => Binário')
    print('\033[32m[2]\033[m - Decimal => Octal')
    print('\033[33m[3]\033[m - Decimal => Hexadecimal')
    esc2 = int(input('Escolha o número: '))
    print(30*'-')
    if esc2 == 1:
        n = int(input('Digite o número: '))
        print(f'O número {n} em decimal é \033[36m{bin(n)[2:]}\033[m')
    elif esc2 == 2:
        n = int(input('Digite o número: '))
        print(f'O número {n} em octal é \033[36m{oct(n)[2:]}\033[m')
    elif esc2 == 3:
        n = int(input('Digite o número: '))
        print(f'O número {n} em hexadecinal é \033[36m{hex(n)[2:]}\033[m')
    else:
        print('Dígito inválido')
if esc1 == 2:
    print('\033[31m[1]\033[m - Binário => Decimal')
    print('\033[32m[2]\033[m - Octal => Decimal')
    print('\033[33m[3]\033[m - Hexadecimal => Decimal')
    esc2 = int(input('Escolha o número: '))
    print(30*'-')
    if esc2 == 1:
        n = int(input('Digite o número: '))
        exp = n
        dec=0
        i=0
        while exp!=0:
            resto = exp%10
            exp = exp//10
            dec = dec + resto*2**i
            i+=1
        print(f'O número binário {n}, em decimal é \033[36m{dec}\033[m')
    elif esc2 == 2:
        n = int(input('Digite o número: '))
        exp = n
        dec=0
        i=0
        while exp!=0:
            resto = exp%10
            exp = exp//10
            dec = dec + resto*8**i
            i+=1
        print(f'O número octal {n}, em decimal é \033[36m{dec}\033[m')
    elif esc2 == 3:
        n = input('Digite o número: ')
        dec=0
        i=0
        new_n=n.upper()
        qtd_letras = len(new_n)
        reverse = new_n[qtd_letras::-1]
        while 'A' in reverse:
            cont = reverse.find('A')
            dec = dec +  10 * 16**(cont)
            reverse = reverse.replace('A','0',1)
            new_n = new_n.replace('A','0')
        while 'B' in reverse:
            cont = reverse.find('B')
            dec = dec + 11 * 16**(cont)
            reverse = reverse.replace('B','0',1)
            new_n = new_n.replace('B','0')
        while 'C' in reverse:
            cont = reverse.find('C')
            dec = dec + 12 * 16**(cont)
            reverse = reverse.replace('C','0',1)
            new_n = new_n.replace('C','0')
        while 'D' in reverse:  
            cont = reverse.find('D')
            dec = dec + 13 * 16**(cont)
            reverse = reverse.replace('D','0',1)
            new_n = new_n.replace('D','0')
        while 'E' in reverse:
            cont = reverse.find('E')
            dec = dec + 14 * 16**(cont)
            reverse = reverse.replace('E','0',1)
            new_n = new_n.replace('E','0')
        while 'F' in reverse:
            cont = reverse.find('F')
            dec = dec + 15 * 16**(cont)
            reverse = reverse.replace('F','0',1)
            new_n = new_n.replace('F','0')
        number = int(new_n)
        exp = number
        while exp!=0:
            resto = exp%10
            exp = exp//10
            dec = dec + resto*16**i
            i+=1
        print(f'O número hexadecimal {n} em decimal é \033[36m{dec}\033[m')
    else:
        print('Dígito inválido')
elif esc1>2:
    print('Dígito inválido')