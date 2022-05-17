n = int(input('Digite um número para\ncalcular seu FATORIAL: '))
f = 1

for c in range(n, 0, -1):
    print('{}'.format(c), end=' ')
    f = f * c
    if c > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
print('{}'.format(f))
