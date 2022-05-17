pessoas = list()
dado = list()
while True:
    dado.append(str(input('NOME: ')).strip().capitalize())
    dado.append(int(input('PESO: ')))
    pessoas.append(dado[:])
    dado.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('Os mais pesados são ', end='')
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]}', end='.. ')
print()
print('Os mais leves são ', end='')
for p in pessoas:
    if p[1] < 65:
        print(f'{p[0]}', end='.. ')