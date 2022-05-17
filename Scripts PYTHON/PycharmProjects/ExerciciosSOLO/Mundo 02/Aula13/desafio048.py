print('{:=^71}'.format('SOMA ÍMPARES'))
s = 0
cont = 0
for c in range(1, 501):                     #(1, 501, 2) OU
    if c % 2 != 0 and c % 3 == 0:           #c % 2 != 0  essas duas opções me filtrará os números impares no intervalo.
        cont = cont + 1
        s = s + c
print('Soma dos {} ímpares múltiplos de 3 é igual a {}'.format(cont, s))