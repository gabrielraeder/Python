print('-='*20)
print('       ANALISADOR DE TRIÂNGULOS')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a+b) > c and (a+c) > b and (b+c) > a:
    print('Os segmentos {}, {} e {} formam um triângulo.'.format(a, b, c))
else:
    print('É impossível formar um triângulo com os valores acima.')
