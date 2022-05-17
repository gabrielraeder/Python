

def leiaDinheiro(msg):
    valido = False
    while not valido:
        v = str(input('Digite o preço: R$ ')).replace(',', '.').strip()
        if v.isalpha() or v == '':
            print(f'\033[1;31mERRO!\033[m')
        else:
            valido = True
            v = float(v)
    return v
