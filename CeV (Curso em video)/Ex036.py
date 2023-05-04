salario = int(input('Digite seu salário: '))
casa = int(input('Digite o valor da casa: '))
tempo = int(input('Digite os anos a ser pago: '))
meses = 12*tempo
prestacao = casa/meses
print(f'O empréstimo da casa ficará R${prestacao:.2f} durante {meses} meses')
if prestacao > salario*0.3:
    print('O empréstimo foi negado, valor muito alto')
else:
    print('Empréstimo aceito')