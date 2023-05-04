print(5*'=','Fatorial',5*'=')
n = int(input('Digite um valor: '))
aux = n
f = n-1
print(15*'=')
while f > 0:
    print(aux,' × ',f,' = ',f*aux)
    aux = f*aux
    f -= 1
print(15*'=')
print(f'{n}! = {aux}')

#for f in range(n-1,0,-1):
    #print(aux,' × ',f,' = ',f*aux)
    #aux = aux*f
#print(15*'=')
#print(f'{n}! = {aux}')   