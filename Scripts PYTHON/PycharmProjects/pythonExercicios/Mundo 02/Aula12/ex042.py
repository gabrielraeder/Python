print('\033[1;30;45m!!! EXERCICIO 035 / CONTINUAÇÃO !!!\033[m')
print('-='*20)
print('       ANALISADOR DE TRIÂNGULOS')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print('Os segmentos {}, {} e {} formam um triângulo.\nE este é um triângulo '.format(a, b, c), end='')
    if a == b and b == c:
        print('EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('ISÓSCELES.')
    elif a != b and b != c and a != c:
        print('ESCALENO.')
else:
    print('Com tais segmentos é impossível formar um triângulo.')
