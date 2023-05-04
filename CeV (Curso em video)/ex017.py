import math
print(5*'=','Hipotenusa',5*'=')
print()
cat = float(input('Digite o valor do primeiro cateto: '))
cat1 = float(input('Digite o valor do segundo cateto: '))
print()
h = math.sqrt(cat**2+cat1**2)
print(f'O valor da hipotenusa é {h:.2f}')