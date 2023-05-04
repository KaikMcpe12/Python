print(f'{"Números Primos":=^30}')
for n1 in range(1,10):
    divisor = 0
    for n2 in range(1,n1+1):
        if n1 % n2 == 0:
            divisor += 1
    if divisor == 2:
        print(n1)