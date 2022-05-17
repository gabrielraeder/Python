real = float(input('Quantos reais você possui? R$'))
dolar = real / 5.40
euro = real / 6.02
libra = real / 7.24
peso = real / 0.051
print('Com R${:.2f} você pode comprar:\n US${:.2f}'.format(real, dolar))
print('  €{:.2f}'.format(euro))
print('  £{:.2f}'.format(libra))
print('  ${:.2f}'.format(peso))
