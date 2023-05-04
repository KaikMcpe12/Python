print(5*'=','Fibonaci',5*'=')
n = int(input('Digite a quantidade de números a ser mostrado: '))
print('Sequência: ')
print(20*'=')
a = 1
b = a
c = b
i = 1
print(a,end=' - ')
while i < n:
    i += 1
    print(a,end=' - ')
    a = b + c
    c = b
    b = a
    #o i foi somado com 1 logo no início, pois se fosse no final iria executar mais de uma vez por ter imprimido uma vez o a
print('FIM')
#o i vai menor que n pois antes do laço de repetição já foi mostrado o primeiro termo