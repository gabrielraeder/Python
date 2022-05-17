temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('NOME: ')).strip().capitalize())
    temp.append(float(input('PESO: ')))
    if len(lista)==0:                   #checagem de peso
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print()
print(f'Ao todo foram cadastrados {len(lista)} pessoas.')
print(f'O maior peso foi {maior}Kg', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='.. ')
print(f'\nO menor peso foi {menor}Kg, de', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='.. ')