maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa (KG): '.format(p)))
    if p == 1:
        maior = maior + peso
        menor = menor + peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior = {}Kg\nMenor = {}Kg'.format(maior, menor))
