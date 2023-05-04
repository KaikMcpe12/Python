n1 = int(input('Digite o valor de N1: '))
n2 = int(input('Digite o valor de N2: '))
esc = 0
while esc != 5:
    print('''\033[33m[1]\033[m - Somar
\033[33m[2]\033[m - Multiplicar
\033[33m[3]\033[m - Maior
\033[33m[4]\033[m - Novos valores
\033[33m[5]\033[m - Sair do programa''')
    print(20*'-')
    esc = int(input('Digite sua escolha: '))
    print(10*'-')
    if esc == 1:
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é {s}')
        print(10*'-')
    elif esc == 2:
        mult = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}')
        print(10*'-')
    elif esc == 3:
         maior = n1
         if maior < n2:
             maior = n2
         elif n1 == n2:
             maior = 'Iguais'
         print('Maior: ',maior)
         print(10*'-')
    elif esc == 4:
         n1 = int(input('Digite o novo valor de N1: '))
         n2 = int(input('Digite o novo valor de N2: '))
         print(10*'-')
    elif esc > 5 or esc < 1:
          print('Valor inválido')
          print(10*'-')
print('ENCERRANDO....')