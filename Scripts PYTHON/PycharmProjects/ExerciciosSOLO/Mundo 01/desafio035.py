a = float(input('valor primeira reta: '))
b = float(input('valor segunda reta: '))
c = float(input('valor terceira reta: '))
if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    print('Os valores {}, {} e {} formam um triângulo!'.format(a, b, c))
    if a == b == c:
        print('EQUILÁTERO')
else:
    print('Os valores {}, {} e {} não podem formar um triângulo.'.format(a, b, c))