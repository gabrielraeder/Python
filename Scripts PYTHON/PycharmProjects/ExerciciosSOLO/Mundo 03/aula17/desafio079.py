lista = list()
while True:
    continuar = ' '
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print(f'Valor {n} adicionado com sucesso.')
    else:
        print('Valor existente, não será adicionado novamente.')

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(sorted(lista))
