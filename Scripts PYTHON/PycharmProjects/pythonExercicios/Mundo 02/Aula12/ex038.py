a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a == b:
    print('Os valores digitados são IGUAIS!')
elif a > b:
    print('O número {} é maior que {}.'.format(a, b))
else:
    print('O número {} é maior que {}.'.format(b, a))