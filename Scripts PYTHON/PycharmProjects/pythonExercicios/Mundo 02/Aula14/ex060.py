n = int(input('Digite um número para\ncalcular seu FATORIAL: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    f = f * c #calculo da fatorial, a cada rodada do loop ele multiplicará pelo vamor anterior de C
    c = c - 1
    if c > 0:
        print('x', end=' ')
    else:
        print('=', end=' ')
print('{}'.format(f))
