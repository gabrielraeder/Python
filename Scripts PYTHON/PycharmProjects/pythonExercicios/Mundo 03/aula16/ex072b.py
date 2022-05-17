tup = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    cont = ' '
    n = int(input('Qual número deseja ver? '))
    if 0 <= n <= 10:
        print(f'o número {n} por extenso é {tup[n]}.')
        while cont not in 'SN':
            cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                print('Tente Novamente')
    else:
        print('Tente Novamente. ', end='')
    if cont == 'N':
        break

print('PROGRAMA ENCERRADO')
