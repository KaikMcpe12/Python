for n1 in range(1,11):
    for n2 in range(1,11):
        print(f'{n1} × {n2} = {n1*n2}',end='       ')  
        if n2 % 3 == 0 or n2==10:
            print('\n')