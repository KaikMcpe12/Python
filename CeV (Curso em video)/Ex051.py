print(5*'=','Progressão Aritmética',5*'=')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
décimo = a1 + (10-1)*r
for pn in range(a1,décimo,r):
    print(pn) 
#for n in range(1,10):
    #pn = a1+(n-1)*r
    #print(pn)   