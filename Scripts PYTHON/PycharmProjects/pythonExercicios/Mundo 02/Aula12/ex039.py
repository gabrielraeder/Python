from datetime import date
print('\033[1;97;42m', '%'*5, 'ALISTAMENTO MILITAR', '%'*5, '\033[m')
print('')
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Quem nasceu em {} faz {} anos em {}.'.format(ano, idade, date.today().year))
if idade < 18:
    if idade == 17:
        print('Falta {} ano para o seu ALISTAMENTO.'.format(18 - idade))
    else:
        print('Faltam {} anos para o seu ALISTAMENTO.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('Você deve se ALISTAR IMEDIATAMENTE!')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos.'.format(date.today().year - (ano+18)))
    print('Seu alistamento foi no ano {}.'.format(ano + 18))
