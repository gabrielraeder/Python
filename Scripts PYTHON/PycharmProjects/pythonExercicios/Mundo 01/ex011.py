l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Sua parede tem a dimensão de {}x{} e sua area é de {:.2f}m².'.format(l, a, area))
print('Para pintar essa parede você precisará de {:.2f} litros de tinta.'.format(area/2))
