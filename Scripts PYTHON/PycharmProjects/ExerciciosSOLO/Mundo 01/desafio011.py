l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a
print('Serão necessários {:.2f} litros de tinta para pintar a parede de {:.2f}m2'.format(area/2, area))
