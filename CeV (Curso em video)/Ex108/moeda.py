def aumentar(rs,n):
    rs = rs + (rs * n/100)
    return rs
def diminuir(rs,n):
    rs = rs - (rs * n/100)
    return rs
def metade(rs):
    return rs / 2
def dobro(rs):
    return rs * 2
def moeda(rs,moeda='R$'):
    return f'{moeda}{rs:>.2f}'.replace('.',',')