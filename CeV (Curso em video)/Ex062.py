print(5*'=','Progressão Aritmética',5*'=')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
t = int(input('Digite a quantidade de termos:  '))
n = 1
while n <= t:
    pn = a1 + r*(n-1)
    print(pn,end=' - ')
    if n == t:
        print('PAUSA')
        print(20*'-')
        c = int(input('Digite quantos termos quer posteriormente: '))
        print(20*'-')
        t+=c
    n+=1
        #a soma de n1 foi declarada logo no final, pois quando n1 chegava a t ele não imprimia o próximo termo e sim executava o if
print(f'Quantidade de termos mostrados: {n-1}')
#n foi subtraído -1 pois quando n era igual a t, n era somado com 1, ficando um a mais que t
print('ENCERRANDO....')