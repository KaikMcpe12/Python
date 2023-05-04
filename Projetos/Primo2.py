primo = 0
list_primo = list()
def prime(n):
    for i in range(2,n//2+1):
        if not(n%i):
            return 0
    return 1
for n in range(100):
    #primo += prime(n)
    if prime(n) == 1:
        list_primo.append(n)
for c in list_primo:
    print(f'{c:<10}',end='')