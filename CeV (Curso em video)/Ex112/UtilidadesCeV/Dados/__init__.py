def leiaDinheiro(msg):
    rs = input(msg).replace(',','.').strip()
    while rs.isalpha() or rs == '':
        print(f'\033[31mERRO! \"{rs}\" é um preço inválido\033[m')
        rs = input(msg).replace(',','.').strip()
    return float(rs)