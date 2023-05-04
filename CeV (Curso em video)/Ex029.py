v = int(input('Digite a velocidade (Km/h) do carro: '))
if v > 80:
    multa = (v-80)*7
    print(f'A multa será de R${multa}')
else:
    print('A velocidade está adequada')