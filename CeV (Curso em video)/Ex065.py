print(5*'=','Sequência de números',5*'=')
resp = 'S'
i = m = s = maior = 0
while resp in 'Ss':
    n = int(input('Digite o número: '))
    resp = input('Quer continuar [S/N]: ')
    if i == 0:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n   
    s += n
    i += 1
m = s/i
print(f'''\n\033[32mMaior -\033[m {maior} 
\033[32mMenor -\033[m {menor}
\033[32mMédia -\033[m {m}''')