s = 0
cont = 0
p = int(input('Informe o primeiro digito: '))
r = int(input('Informe a razão da P.A.: '))
décimo = p + (10) * r
for c in range(p, décimo, r):
    print('{}'.format(c), end='--')
print('......')
