km = float(input('Quantos quilometros foram rodados? '))
d = int(input('Por quantos dias foi alugado? '))
c = (km*0.15) + (d*60)
print('Valor a ser pago pelo aluguel de {} dias, com {:.1f} quilometros rodados é R${:.2f}'.format(d, km ,c))
