from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
id = atual-nasc
print(f'O atleta tem {id} anos.')
if id <=9:
    print('Classificação MIRIM')
elif id>9 and id<=14:
    print('Classificação INFANTIL')
elif id>14 and id<=19:
    print('Classificação JUNIOR')
elif id>19 and id<=25:
    print('Classificação SENIOR')
else:
    print('Classificação MASTER')