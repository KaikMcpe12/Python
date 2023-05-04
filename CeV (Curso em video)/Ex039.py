from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
id = ano-nasc
if id<18:
    print(f'Você falta {18-id} anos para se alistar')
elif id>18:
    print(f'Você passou {id-18} anos da idade de se alistar')
else:
    print('Está na hora de se alistar')