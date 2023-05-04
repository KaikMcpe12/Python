km = int(input('Digite a distância (Km) da viagem: '))
if km <= 200:
    valor = km*0.5
    print(f'Você pagará R${valor}')
else:
    valor = km*0.45
    print(f'Você pagará R${valor}')