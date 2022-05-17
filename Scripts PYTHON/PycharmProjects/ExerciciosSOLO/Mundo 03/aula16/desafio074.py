from random import randrange
tupla = (randrange(10), randrange(10), randrange(10), randrange(10), randrange(10))

print(f'Os sorteados foram {tupla[0]}, {tupla[1]}, {tupla[2]}, {tupla[3]} e {tupla[4]}')
menor = tupla[0]
maior = tupla[0]
for c in tupla:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'MAIOR = {maior}\nMENOR = {menor}')

