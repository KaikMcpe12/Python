carac = []
exp = input('Digite a expressão: ')
for c in exp:
    if c == '(':
        carac.append('(')
    elif c == ')':
         if len(carac) > 0:
             carac.pop()
         else:
             carac.append(')')
             break
if len(carac) > 0:
    print('A expressão é inválida')
else:
    print('A expressão é válida')