s = 0
cont = 0
imp = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
    else:
        imp = imp + 1
print('A soma de {} nº PARES é igual a {}.'.format(cont, s))
print('Impares = {}'.format(imp))