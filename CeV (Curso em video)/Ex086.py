matriz = [[],[],[]]
for c in range(0,3):
    for i in range(0,3):
        matriz[c].append(int(input(f'Digite o valor da posição [{c} {i}]: ')))
print(30*'=')
for c in range(0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]',end=' ')
    print()

#Nota: Na linha 4 poderia colocar (matriz[c][i]), porém teria predefinir os valores da matriz, pois isso irá apenas substituir os valores que já estão na lista e não adicionar. Seria preciso atribuir (matriz[[0,0,0],[0,0,0],[0,0,0]])