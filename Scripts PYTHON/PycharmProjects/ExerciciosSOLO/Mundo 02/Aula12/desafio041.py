from datetime import date
print('%'*5, '\033[1;31mCONFEDERAÇÃO DE NATAÇÃO\033[m', '%'*5)
print('')
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria MIRIM')

elif 9 < idade <= 14:
    print('Categoria INFANTIL')

elif 14 < idade <= 19:
    print('Categoria JUNIOR')

elif 19 < idade <= 20:
    print('Categoria SÊNIOR')

else:
    print('Categoria MASTER')
print('')
print('%'*15, '\033[1;32mFIM\033[m', '%'*15)