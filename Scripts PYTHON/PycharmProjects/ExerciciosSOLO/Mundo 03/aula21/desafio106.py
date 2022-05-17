
def ajuda(msg):
    from time import sleep
    tx1 = ' Sistema de ajuda PyHELP '
    while True:
        print('\033[1;30;42m~\033[m' * len(tx1))
        print(f'\033[1;30;42m{tx1}\033[m')
        print('\033[1;30;42m~\033[m' * len(tx1))
        sleep(.4)
        n = str(input(msg)).lower().strip()

        if n == 'fim':
            break
        else:
            sleep(.6)
            tx2 = f'  Acessando o manual do comando {n}  '
            print('\033[1;30;43m~\033[m' * len(tx2))
            print(f'\033[1;30;43m{tx2}\033[m')
            print('\033[1;30;43m~\033[m' * len(tx2))
            print('\033[1;30;107m')
            sleep(.6)
            print(f'\033[1;30;107m{help(n)}\033[m')
            sleep(.6)



n = ajuda('Função ou Biblioteca -> ')