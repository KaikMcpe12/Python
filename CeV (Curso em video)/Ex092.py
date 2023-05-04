from datetime import datetime
dados = dict()
dados['Nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: '))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - nasc
print(30*'=')
print('==Dados==')
for k,v in dados.items():
    print(f'    -{k} é igual a {v}')