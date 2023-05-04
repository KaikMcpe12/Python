l1 = int(input('Digite o valor do lado L1: '))
l2 = int(input('Digite o valor do lado L2: '))
l3 = int(input('Digite o valor do lado L3: '))
print(20*'=')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados digitados podem formar um triângulo')
    print(20*'=')
    if l1== l2 == l3:
        print('O triângulo é equilátero')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print('Os lados digitados não podem formar um triângulo')