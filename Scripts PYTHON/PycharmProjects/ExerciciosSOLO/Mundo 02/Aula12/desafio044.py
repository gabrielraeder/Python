print('$'*5, '\033[7;32;107mCALCULO DE DESCONTO\033[m', '$'*5)
print()
v = float(input('Informe o preço do produto: R$'))
f = str(input('Informe a forma de pagamento: '))
if f == 'à vista':
    print('Com 10% de desconto o preço a pagar será R${:.2f}.'.format(v-(v*10/100)))
elif f == 'cartão':
    print('No cartão com 5% de desconto o valor será R${:.2f}.'.format(v-(v*5/100)))
elif f == '2x':
    print('Parcelado em 2 vezes no cartão o valor será R${:.2f}.'.format(v))
else:
    print('Parcelado em 3 ou mais vezes terá um juros de 20% e o valor será R${:.2f}.'.format(v + (v*20/100)))
print()
print('$'*13, '\033[7;32;107mFIM\033[m', '$'*13)
