def notas(*n,sit = False):
    """
    ->Função para analisar notas e situação de vários alunos
    param n: Uma ou mais notas dos alunos (Aceita vários)
    param sit: valor opcional, indicado se deve ou não mostrar a situação
    return: Dicionário com várias informação sobre a situação da turma    """
    dic = {}
    dic["Total"] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        if dic['Média'] < 6:
            dic['Situação'] = 'RUIM'
        elif 6 >=dic['Média'] < 7:
            dic['Situação'] = 'RAZOAVEL'
        else:
            dic['Situação'] = 'BOA'
    return dic
resp = notas(8,8,8,sit = True)
print(resp)