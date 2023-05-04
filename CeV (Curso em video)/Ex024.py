city = input('Digite o nome de sua cidade: ')
task = city.upper().split()
if 'SANTOS' in task[0]:
    print(f'A cidade {city} começa com Santos ')
else:
    print(f'A cidade {city} não começa com Santos')