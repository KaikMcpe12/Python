print(5*'=','Número de 0 - 999: ',5*'=')
c = s = 0
n = int(input('Digite o número sorteado: '))
print(15*'-')
while n != 999:
    s = s + n
    c += 1
    n = int(input('Você errou, digite novamente: '))
    print(15*'-')
print('Você acertou!!!!!')
print(f'Tentativas: {c}')
print(f'Soma: {s}')