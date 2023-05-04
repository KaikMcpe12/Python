import math
print(5*'=','Parte inteira',5*'=')
print()
num = float(input(' Digite um número para que mostre apenas sua parte inteirar: '))
num1 = math.trunc(num)
print()
print(f'A parte inteira de {num} é {num1}')