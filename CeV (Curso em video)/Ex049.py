print(5*'=','Tabuada',5*'=')
x = int(input('Digite o valor para descobrir sua tabuada: '))
print('\033[31;1mSoma:\033[m')
for s in range(1,11):
    print(x,' + ',s,' = ',s+x)
print('\033[31;1mSubtração\033[m')
for sub in range(1,11):
    print(x,' - ',sub,' = ',x-sub)
print('\033[31;1mMultiplicação\033[m')
for mult in range(1,11):
    print(x,' × ',mult,' = ',mult*x)
print('\033[31;1mDivisão\033[m')
for div in range(1,11):
    print(x,' ÷ ',div,' = ',x/div)