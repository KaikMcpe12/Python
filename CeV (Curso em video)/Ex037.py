print('''\033[31m[0]\033[m Decimal => Binario
\033[32m[1]\033[m Decimal => Octal
\033[33m[2]\033[m Decimal => Hexadecimal''')
print(20*'=')
esc = int(input('Digite sua escolha: '))
print(20*'=')
if esc==0:
    num = int(input('Digite o número: '))
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif esc==1:
    num = int(input('Digite o número: '))
    print(f'O número {num} em Octal é {oct(num)[2:]}')
elif esc==2:
    num = int(input('Digite o número: '))
    print(f'O número {num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Dígito inválido')