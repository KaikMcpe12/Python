def escreva(msg):
    comp = len(msg) + 4
    print(comp*'~')
    print(f'{msg:^{comp}}')
    print(comp*'~')

escreva("Gustavo Guanabara")
escreva("Curso de Python no YouTube")
escreva("CeV")