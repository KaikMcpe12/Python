print(5*'=','Progressão Aritmética',5*'=')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
n = 1
while n <=10:
    pn = a1 + r*(n-1)
    n+=1
    print (pn,end=' - ')