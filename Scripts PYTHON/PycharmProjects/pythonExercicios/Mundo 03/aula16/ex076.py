lista = ('Caneta', 1.90, 'Lápis', 0.99, 'Caderno', 11.49, 'Borracha', 0.50, 'Giz', 29,
         'lapiseira', 5, 'Grampos', 9.90, 'Régua', 15.29, 'Livro', 55)
print('-'*35)
print(f'{" PREÇOS ":|^35}')
print('-'*35)
for posição in range(0, len(lista)):
    if posição % 2 == 0:
        print(f'{lista[posição]:.<25}', end='')
    else:
        print(f'R$ {lista[posição]: >6.2f}')
print('-' * 35)
