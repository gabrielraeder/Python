print('$'*5, '\033[1;43mCOMPLEMENTO EX035\033[m', '$'*5)
print('')
a = float(input('Valor primeira reta: '))
b = float(input('Valor segunda reta: '))
c = float(input('Valor terceira reta: '))
if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    print('Os valores {}, {} e {} formam um triângulo!'.format(a, b, c))
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    elif a != b != c:
        print('ESCALENO')
else:
    print('Os valores {}, {} e {} não podem formar um triângulo.'.format(a, b, c))

print('')
print('$'*9, '\033[1;43mENCERRADO\033[m', '$'*9)
