from time import sleep
print('|'*25)
print('|'*8, '\033[1;30;42mVIAGENS\033[m', '|'*8)
print('|'*25)
d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('Sua viagem de {}km custará...'.format(d), end='')
sleep(2)
print('R${:.2f}'.format(preço))
