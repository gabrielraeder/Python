n = int(input('Informe um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;32m', end='')
        tot = tot + 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[4;97;42m NÚMERO PRIMO \033[m')
