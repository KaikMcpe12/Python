nome = input(' Digite seu nome completo: ')
print(f'Seu nome em maiúsculo é:\n{nome.upper()}')
print(f'Seu nome em minúsculo é:\n{nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ",""))} letras')
nome1 = nome.split()
print(f'Seu primeiro nome é {nome1[0]} e tem {len(nome1[0])} letras')