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