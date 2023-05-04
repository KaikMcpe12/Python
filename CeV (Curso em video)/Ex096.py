def área(l,b):
    área = b * l
    print(f'A área de um terreno {l}×{b} é de {área}')
print(f'{"Controle de Terrenos":^30}')
print(30*'-')
larg = float(input('LARGURA (m): '))
base = float(input('COMPRIMENTO (m): '))
área(larg,base)