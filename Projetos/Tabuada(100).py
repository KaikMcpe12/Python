for n1 in range(1,101):
    for n2 in range(1,101):
        print(f'{n1} × {n2} = {n1*n2}',end='       ')  
        if n2 % 3 == 0 or n2==100:
            print('\n')