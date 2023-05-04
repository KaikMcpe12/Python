altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/altura**2
print(15*'=')
print(f'Seu IMC é {imc:.2f}')
if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<40:
    print('Obesidade')
else:
    print('Obesidade mórbida')