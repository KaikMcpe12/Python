matriz = [[],[],[]]
s_pares = s_col3 = 0
for c in range(0,3):
    for i in range(0,3):
        matriz[c].append(int(input(f'Digite o valor da posição [{c} {i}]: ')))
print(30*'=')
for c in range(0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]',end=' ')
        if matriz[c][i] % 2 == 0:
           s_pares += matriz[c][i]
    if c == 0:
        m_row3 = matriz[1][c]
    elif matriz[1][c] > m_row3:
        m_row3 = matriz[1][c]
    s_col3 += matriz[c][2]
    print()
print(30*'=')    
#m_row3 = max(matriz[1])
print(f'A soma dos valores pares é {s_pares}')
print(f'A soma dos valores da terceira coluna é {s_col3}')
print(f'O maior valor da terceira coluna é {m_row3}')