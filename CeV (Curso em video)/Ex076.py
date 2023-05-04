listagem = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.90)
print(30*'=')
print(f'{"Listagem de preços":^30}')
print(30*'=')
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20}',end='')
    else:
        print(f'R${listagem[c]:>5.2f}')
print(30*'=')