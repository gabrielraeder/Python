def leiaDinheiro(msg):
    valido = False
    while not valido:
        n = str(input(msg)).replace(',','.').strip()
        if n.isalpha() or n == '':
            print(f'\033[1;31mERRO!\033[m')
        else:
            valido = True
    return float(n)

