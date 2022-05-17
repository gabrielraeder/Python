s = 0
cont = 0
for c in range(1, 501, 3):      #(,,3) filtra os números divisiveis por 3, (1,,2) filtra os números impares.
    if c % 2 != 0:
        s = s + c
        cont = cont + 1
print('Existem {} ímpares multiplos de 3 no intervalo, e a soma destes é {}.'.format(cont, s))
