from lib.interface import *

def ArqExiste(nome):
    try:
        n = open(nome,'rt')
        n.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriaArq(nome):
    try:
        n = open(nome,'wt+')
        n.close()
    except:
        print('\033[31mHouve um erro ao criar o arquivo\033[m')
    else:
        print('Arquivo criado com sucesso')
        
def LerArq(arq):
    try:
        n = open(arq,'rt')
    except:
        print('\033[31mERRO ao abrir o arquivo\033[m')
    else:
        título('MOSTRAR PESSOAS CADASTRADAS')
        for linha in n:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        n.close()
        
def Cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        n = open(arq,'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            n.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO Erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            n.close()             