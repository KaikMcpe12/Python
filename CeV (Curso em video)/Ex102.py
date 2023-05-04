def Fatorial (n , show = False):
    """
    -> Calcula o Fatorial de um número
    param n: O número a ser calculado
    param show: (opcional) Mostrar ou não a conta
    return : O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            if c > 1:
                print(c,end = ' × ')
            else:
                print(c,end = ' = ')
        f *= c
    return f
print(Fatorial(5,True))