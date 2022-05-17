p = int(input('Informe o primeiro digito: '))
r = int(input('Informe a razão da P.A.: '))
cont = 1
termo = p
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='')
        if cont < total:
            print(' - ', end='')
        termo = termo + r
        cont = cont + 1
    print('')
    mais = int(input(('Quantos termos a mais? ')))
print('Foram exibidos um total de {} termos.'.format(total))
print('')
print('FIM')













'''perg = str(input('Deseja mostrar mais termos? [S/N] ')).strip().upper()
if perg == 'N':
    print('ENCERRADO')
elif perg == 'S':
    op = int(input('Quantos termos deseja? '))
    q = 10 + op
    while cont <= q:
        print('{}'.format(p), end='')
        if cont < q:
            print(' - ', end='')
        cont = p
        p = p + r
        cont = cont + 1
print('\n')
print('FIM')'''