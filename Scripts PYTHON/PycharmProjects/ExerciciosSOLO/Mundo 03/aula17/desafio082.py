lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)

print(f'Você digitou: {sorted(lista)}')
print(f'PARES: {sorted(par)}')
print(f'IMPARES: {sorted(impar)}')