def aumentar(rs,n,f = False):
    rs = rs + (rs * n/100)
    return rs if not f else moeda(rs)

def diminuir(rs,n,f = False):
    rs = rs - (rs * n/100)
    return rs if not f else moeda(rs)

def metade(rs, f = False):
    return rs / 2 if not f else moeda(rs/2)

def dobro(rs, f = False):
    return rs * 2 if not f else moeda(rs*2)

def moeda(rs,moeda='R$'):
    return f'{moeda}{rs:>.2f}'.replace('.',',')
    
def resumo(rs,taxaa = 0, taxar = 0):
    print(30*'=')
    print('RESUMO DOS VALORES'.center(30))
    print(30*'=')
    print(f'Preço analisado: \t{moeda(rs)}')
    print(f'Dobro do preço: \t{dobro(rs,True)}')
    print(f'Metade do preço: \t{metade(rs,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(rs,taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminuir(rs,taxar,True)}')
    print(30*'=')