import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível\033[m')
else:
    print('\033[33mO site Pudim está acessível\033[m')
    #print(str(site.read()).replace('\\n','\n')) #->Irá ler o site (o código)