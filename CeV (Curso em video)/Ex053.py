print(5*'=','Detector de palindromo',5*'=')
frase = input('Digite a frase:\n\033[33m')
print('\033[m')
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(junto,' => ',inverso)
if inverso == junto:
    print('A palavra é palindromo')
else:
    print('A palavra não é um palindromo')










#nfrase = frase.replace(' ','')
#cont = len(nfrase)
#reverse = nfrase[cont::-1]
#if nfrase == reverse:
    #print('A frase é palindromo')
#else:
    #print('A frase não é palindromo')