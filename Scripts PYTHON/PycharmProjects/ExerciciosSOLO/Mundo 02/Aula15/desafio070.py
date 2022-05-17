s = 0
mil = 0
barato = 999999999999999999999
prodbarato = 'a'
print('$' * 30)
while True:
    prod = str(input('Nome produto: ')).strip().upper()
    preço = float(input('Preço: R$ '))
    print('$' * 30)
    s = s + preço
    if preço < barato:
        barato = preço
        prodbarato = prod
    if preço > 1000:
        mil = mil + 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('$' * 30)
    if continuar in 'N':
        break
print(f'TOTAL = R$ {s:.2f}\nAcima de mil = {mil} itens\nProduto mais barato = {prodbarato}')


