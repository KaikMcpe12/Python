números = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'O número {n} em extenso é {números[n]}')