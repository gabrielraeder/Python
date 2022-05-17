print('\033[1;97;40m=\033[m'*6, '\033[4;30;43mCOMPARADOR DE VALORES\033[m', '\033[1;97;40m=\033[m'*5)
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O primeiro valor, {}, é maior.'.format(a))
elif a < b:
    print('O segundo valor, {}, é o maior.'.format(b))
else:
    print('Os valores são iguais.')