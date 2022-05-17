from datetime import date
print('\033[1;30;44m+++ NATAÇÃO +++\033[m')
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('A atleta tem \033[1;30;107m{}\033[m anos.\nE sua categoria é:'.format(idade))
if idade < 9:
    print('\033[1;36;40m  MIRIM  \033[m')
elif 9 <= idade < 14:
    print('\033[1;34;40m  INFANTIL  \033[m')
elif 14 <= idade < 19:
    print('\033[1;31;40m  JÚNIOR  \033[m')
elif 19 <= idade < 25:
    print('\033[1;32;40m  SÊNIOR  \033[m')
elif idade >= 25:
    print('\033[1;97;40m  MASTER  \033[m')