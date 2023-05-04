n = '1aa'
#decimal
dec=0
#expoente
i=0
#transforma a string em maiúsculo
new_n=n.upper()
#quantidade de letras
qtd_letras = len(new_n)
#reverte a string, sendo que o 0 era primeiro termo, agora será o último
reverse = new_n[qtd_letras::-1]
#laço que servirá para seja substituída todas as letras A, uma por uma, não será substituída tudo de uma vez por contabilizar apenas a primeira letra repetida
while 'A' in reverse:
    #irá encontrar a posição do A na string invertida
    cont = reverse.find('A')
    #a posição irá servir como expoente e a segunda variável dec é para somar com os valores anteriores, nesse caso a segunda variável dec irá servir apenas para 'enfeite'
    dec = dec +  10 * 16**(cont)
    #essa substituição irá fazer com que o primeiro A na string invertida seja substituída por 0 que será posteriormente o mesmo que nada
    #essa substituição por parte se dá pelo fato de alguns casos haver mais de duas letras iguais e será contabilizada apenas a primeira. Dessa forma irá repetir o processo letra por letra
    #na segunda vez (caso tenha dois A) que se repetir a posição não será a mesma e consequente será o outro A que será substituído
    reverse = reverse.replace('A','0',1)
    #a string oficial será substituída seguindo o mesmo critério que a anterior, Só que por completo, pois a string oficial não está sendo usada nesse processo por enquanto 
    new_n = new_n.replace('A','0')
while 'B' in reverse:
    cont = reverse.find('B')
    dec = dec + 11 * 16**(cont)
    reverse = reverse.replace('B','0',1)
    new_n = new_n.replace('B','0')
while 'C' in reverse:
    cont = reverse.find('C')
    dec = dec + 12 * 16**(cont)
    reverse = reverse.replace('C','0',1)
    new_n = new_n.replace('C','0')
while 'D' in reverse:  
    cont = reverse.find('D')
    dec = dec + 13 * 16**(cont)
    reverse = reverse.replace('D','0',1)
    new_n = new_n.replace('D','0')
while 'E' in reverse:
    cont = reverse.find('E')
    dec = dec + 14 * 16**(cont)
    reverse = reverse.replace('E','0',1)
    new_n = new_n.replace('E','0')
while 'F' in reverse:
    cont = reverse.find('F')
    dec = dec + 15 * 16**(cont)
    reverse = reverse.replace('F','0',1)
    new_n = new_n.replace('F','0')
number = int(new_n)
#variável auxiliar
exp = number
#essa laço irá se repetir até que a variável auxiliar se torne 0 depois de sucessivas divisões
while exp!=0:
    #esse cálculo irá pegar o primeiro número a direita 
    resto = exp%10
    #e como exp está recebendo sua divisão por 10, na segunda vez que repetir ele irá pegar o segundo valor a direita do valor inicial
    exp = exp//10
    #irá somar os valores atribuidos a dec nós processos anteriores com o 16 elevado a quantas vezes o while se repetiu
    #na primeira vez o expoente será zero, na segunda ele pegará o segundo número a direita e o expoente(i) se tornará 1
    dec = dec + resto*16**i
    i+=1
print(dec)