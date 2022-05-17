lista = list()
maior = menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um número na {c+1}ª posição: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('+'*50)
print(f'Você digitou os valores {sorted(lista)}')
print('+'*50)
print(f'Maior valor = {maior}, Posições = ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}', end='... ')
print()
print(f'Menor valor = {menor}, Posições = ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}', end='... ')
print()
