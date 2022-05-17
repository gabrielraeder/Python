from time import sleep
print('|'*25)
print('|'*8, '\033[1;30;42mVIAGENS\033[m', '|'*8)
print('|'*25)
print('')
d = float(input('Qual é a distância da sua viagem? '))
preço = d * 0.50 if d <= 200 else d * 0.45
print('Sua viagem de {}km custará...'.format(d), end='')
sleep(1)
print('R${:.2f}'.format(preço))