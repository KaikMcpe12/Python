times = ('Palmeiras','Internacional','Flamengo','Corinthians','Fluminense','Athletico-PR','Atlético-MG','São Paulo','América-MG','Fortaleza','Botafogo','Santos','Bragantino', 'Goiás','Coritiba','Ceará SC','Atlético-GO','Cuiabá','Avaí','Juntude')
print(f'Lista dos times do brasileirão: {times}')
print(30*'=')
print(f'Os 5 primeiros são: {times[:5]}')
print(30*'=')
print(f'Os 4 últimos são: {times[-4:]}')
print(30*'=')
print(f'Times em ordem alfabética: {sorted(times)}')
print(30*'=')
print(f"O Ceará está na {times.index('Fortaleza')+1}° posição")