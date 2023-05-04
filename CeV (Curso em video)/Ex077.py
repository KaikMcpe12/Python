palavras = ('aprender','programar','linguagem','python','curso','grátis','estudar','praticar','trabalhar','mercado','programador','futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} existe as vogais: ',end='')
    for letra in c:
        if letra.upper() in 'AÁEIOU':
            print(letra,end=' ')