p = int(input('Informe o primeiro digito: '))
r = int(input('Informe a razão da P.A.: '))
termo = p
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    if cont < 10:
        print(' - ', end='')
    termo = termo + r
    cont = cont + 1

