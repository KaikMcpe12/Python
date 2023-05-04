sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Dados inválido, digite novamente: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')