n = int(input('N1: '))
hex = []
while True:
    resto = n % 16
    n = n // 16
    if resto == 10:
        resto = 'a'
    if resto == 11:
        resto = 'b'
    if resto == 12:
        resto = 'c'
    if resto == 13:
        resto = 'd'
    if resto == 14:
        resto = 'e'
    if resto == 15:
        resto = 'f'
    hex.append(resto)
    if n == 0:
        break
print('Hexadecimal: ',end='')
hex.reverse()
for c in hex:
    print(c,end='')