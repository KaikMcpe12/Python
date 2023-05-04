nome = 'Kaik'
cores = {'limpa' : '\033[m' ,
'azul' : '\033[34m' ,
'vermelho' : '\033[31m',
'amarelo' : '\033[33m' ,
'verde' : '\033[32m',
'azul' : '\033[34m',
'pretoebranco' : '\033[1;30m' }
print('{}Olá!{} {}Muito prazer{} {}em te conhecer,{} {}{}!{} '.format(cores['vermelho'],cores['limpa'],cores['amarelo'],cores['limpa'],cores['azul'],cores['limpa'],cores['verde'] , nome , cores['limpa']))