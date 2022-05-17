lista = ('Caderno', 9.90, 'Lapiseira', 2.49, 'Livro', 35, 'Mouse', 49.90, 'Teclado', 100)
print('$'*40)
print(f'{" LISTA DE PREÇOS ": ^40}')
print('$'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]: >8.2f}')
print('='*40)
