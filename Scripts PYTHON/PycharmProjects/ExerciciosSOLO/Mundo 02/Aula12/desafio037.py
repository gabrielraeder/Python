num = int(input('Informe um número: '))
op = int(input('Veja este número em (1)BINÁRIO\n                    (2)OCTAL\n                    (3)HEXADECIMAL: '))
if op == 1:
    print('O valor {} em binário é {}.'.format(num, bin(num)))
elif op == 2:
    print('O valor {} em octal é {}.'.format(num, oct(num)))
else:
    print('O valor {} em hexadecimal é {}.'.format(num, hex(num)))

