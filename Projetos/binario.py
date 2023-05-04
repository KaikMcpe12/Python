n = 111
exp = n
dec=0
i=0
while exp!=0:
    resto = exp%10
    exp = exp//10
    dec = dec + resto*2**i
    i+=1
print(dec)