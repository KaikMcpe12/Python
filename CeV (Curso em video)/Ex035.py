l1 = int(input('Digite o valor do lado L1: '))
l2 = int(input('Digite o valor do lado L2: '))
l3 = int(input('Digite o valor do lado L3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados digitados podem formar um triângulo')
else:
    print('Os lados digitados não podem formar um triângulo')