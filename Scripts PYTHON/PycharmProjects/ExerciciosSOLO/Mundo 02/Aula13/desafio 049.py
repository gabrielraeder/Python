from time import sleep
print('\033[1;30;42m{:=^25}\033[m'.format('TABUADA'))
n = int(input('informe um número: '))
for c in range (1, 11):
    result = n * c
    print('{} x {} = {}'.format(n, c, result))
    sleep(1)
