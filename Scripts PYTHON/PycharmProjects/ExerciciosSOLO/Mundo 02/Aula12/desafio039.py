from datetime import date
print('*'*6, '\033[4;97mALISTAMENTO MILITAR\033[m', '*'*6)
print('')
ano = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda se alistará e seu alistamento ocorrerá daqui a {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar JÁ!!')
else:
    print('Você deveria ter se alistado a {} anos atrás.'.format(idade - 18))
print('')
print('*'*11, '\033[4;97mENCERRADO\033[m', '*'*11)