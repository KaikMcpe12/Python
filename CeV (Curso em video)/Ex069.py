print(5*'=','Cadastro',5*'=')
maior = homens = F_menor = 0
c = 1
while True:
    idade = int(input(f'Idade ({c}°): '))
    sexo = input(f'Sexo ({c}°)[M/F]: ').upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        F_menor += 1
    print(15*'=')
    esc = ' '
    while esc not in 'SN':
        esc = input('Deseja continuar [S/N]? ').upper()
    print(15*'=')
    if esc == 'N':
        print('ENCERRANDO...')
        break
    c += 1
print(f'''\n\033[33mPessoas maiores de 18:\033[m {maior}
\033[33mHomens:\033[m {homens}
\033[33mMulheres menores de 20:\033[m {F_menor}''')