s = 0
for c in range(1, 7):
    n = int(input('{}º número: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('A soma dos pares é {}.'.format(s))