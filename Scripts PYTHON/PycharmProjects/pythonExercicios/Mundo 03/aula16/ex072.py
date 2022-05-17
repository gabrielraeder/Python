tup = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = -1
while True:
    n = int(input('Qual número deseja ver? '))
    if 0 <= n <= 10:
        print(f'o número {n} por extenso é {tup[n]}.')
    else:
        print('Tente Novamente. ', end='')
    cont = ' '
    if 0 <= n <= 10:
        if cont not in 'SN':
            cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                print('Tente Novamente')
            if cont == 'N':
                break
print('PROGRAMA ENCERRADO')
