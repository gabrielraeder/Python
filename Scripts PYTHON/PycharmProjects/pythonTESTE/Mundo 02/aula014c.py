n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        if n % 2 != 0:
            impar = impar + 1
print('PARES = {}\nIMPARES = {}'.format(par, impar))
print(('FIM'))