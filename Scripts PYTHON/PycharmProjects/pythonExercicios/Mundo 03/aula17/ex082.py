lista = []
par = []
impar = []
while True:
    lista.append(int(input('>>>> Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
lista.sort()
for item in lista:
    if item % 2 == 0:
        par.append(item)
    elif item % 2 != 0:
        impar.append(item)
print(f'Lista = {lista}')
print(f'PARES = {par}')
print(f'IMPARES = {impar}')
