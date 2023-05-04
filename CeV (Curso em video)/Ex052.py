print(5*'=','Primo',5*'=')
n = int(input('Digite um número: '))
divisor =0
for c in range(1,n+1):
    if n%c==0:
        divisor+=1
if divisor ==2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')