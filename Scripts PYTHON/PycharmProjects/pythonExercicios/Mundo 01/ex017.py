from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa deste medirá {:.2f}'.format(hip))
hipo = (co**2 + ca**2)**(1/2)
print(hipo)
