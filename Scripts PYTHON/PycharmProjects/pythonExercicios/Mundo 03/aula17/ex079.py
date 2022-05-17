lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print(f'Número {n} adicionado com SUCESSO.')
    else:
        print(f'DUPLICADO! {n} não será incluído novamente.')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort()
print(f'Ordem crescente = {lista}')
