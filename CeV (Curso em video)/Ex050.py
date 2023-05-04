print(5*'=','Soma dos pares',5*'=')
s=0
for n in range (1,7):
    number = int(input(f'Digite o {n}° número: '))
    if number%2==0:
        s+=number
print(f'A soma de todos os pares é {s}')