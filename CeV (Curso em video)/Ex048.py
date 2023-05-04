print(3*'=','Soma dos ímpares múltiplos de três entre 1 e 500',3*'=')
s=0
c=0
for n1 in range(1,501,2):
    if n1%3==0:
        s+=n1
        c+=1
print(f'A soma de todos {c} valores é {s}')