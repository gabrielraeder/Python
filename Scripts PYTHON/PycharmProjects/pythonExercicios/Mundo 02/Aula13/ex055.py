maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso {}ª pessoa (Kg) = '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('MAIOR PESO = {} Kg\nMENOR PESO = {} Kg'.format(maior, menor))
