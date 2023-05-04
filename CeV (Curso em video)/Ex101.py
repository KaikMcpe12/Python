from datetime import date
def voto(nasc):
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
print(30*'=')
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))