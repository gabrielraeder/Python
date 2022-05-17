from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
print('O ângulo de {}º tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))
