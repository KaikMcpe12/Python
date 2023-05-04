print(3*'=','Pintando uma parede',3*'=')
print()
larg = int(input('Digite a largura de uma parede: '))
comp = int(input('Digite o comprimento: '))
tinta = (comp*larg)//2
res =  (comp*larg)%2
print()
print(f'Sabendo que cada lata de tinta pinta 2m² será preciso {tinta+res} baldes de tintas para pintar {comp*larg}m² e sobra {res}m² de tinta no balde')