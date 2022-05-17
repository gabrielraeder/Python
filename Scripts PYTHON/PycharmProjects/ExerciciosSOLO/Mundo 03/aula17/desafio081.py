lista = list()
cont = 0
print('~'*45)
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = cont + 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('~'*45)
    if continua == 'N':
        break
print(f'Foram digitados {cont} números.')
print('~'*45)
print(sorted(lista, reverse=True))
print('~'*45)
if 5 in lista:
    print('O valor 5 está na lista nas posições: ', end=' ')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i+1}', end='... ')
else:
    print('O valor 5 não foi digitado')
print('\n','~'*45)

