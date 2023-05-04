n = int(input('N1: '))
bin = []
while True:
    resto = n % 2
    n = n // 2
    bin.append(resto)
    if n == 0:
        break
print('Binário: ',end='')
bin.reverse()
for c in bin:
    print(c,end='')