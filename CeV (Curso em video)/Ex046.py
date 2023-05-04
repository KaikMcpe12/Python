from time import sleep
print(5*'=','Contagem para o Ano Novo',5*'=')
print('\n\033[36;1mContagem:\033[m')
for c in range(10,-1,-1):
    sleep(1)
    print('\033[1m',c,'\033[m')
print('\033[31;1mFeliz ano NOVO!!!\033[m')