from datetime import date
print('#'*24)
print('   \033[1;32mO ANO É BISSEXTO?\033[m')
print('#'*24)
ano = int(input('Que ano deseja analisar? (coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
