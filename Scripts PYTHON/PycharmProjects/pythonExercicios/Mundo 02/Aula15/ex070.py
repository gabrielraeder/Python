s = tot1k = cont = menor = 0
barato = ' '
while True:
    prod = str(input('Nome do Produto: ')).strip().capitalize()
    preço = float(input('Preço: R$ '))
    cont = cont + 1
    s = s + preço
    if preço >= 1000:
        tot1k = tot1k + 1
    if cont == 1 or menor > preço:
        menor = preço
        barato = prod
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total gasto de R$ {s:.2f}.')
print(f'Temos {tot1k} produto custando acima de R$ 1000,00')
print(f'O produto mais barato é {barato} e custou R$ {menor:.2f}.')