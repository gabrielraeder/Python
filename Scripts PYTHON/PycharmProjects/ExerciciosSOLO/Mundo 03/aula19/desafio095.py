lista = []
while True:

    dic = {'nome':str(input('Nome do Jogador: ')).strip().capitalize()}
    x = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    gols = list()
    totg = 0
    for c in range(1, x+1):
        gol = int(input(f'Quantos gols na {c}ª partida? '))
        totg = totg + gol
        gols.append(gol)
    dic['gols'] = gols[:]
    dic['total'] = totg
    lista.append(dic.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(lista)
print('#'*40)
print(f' {"no.":<4}{"NOME":<10}{"Gols":>8}{"Total":>16}')
print('~'*40)
for i, c in enumerate(lista):
    print(f'{i:<4}{c["nome"]:<18}{c["gols"]}{c["total"]:>16}')
r = 0
while True:
    r = int(input('Mostrar dados de qual jogador? '))
    if r <= len(lista):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[r]["nome"]}:')
        for c in range(0, len(dic['gols'])):
            print(f' => Na {c + 1}ª partida, fez {lista[c]["gols"]} gols.')
        print(f'Foi um total de {lista[r]["total"]} gols.')
    elif r == 999:
        break
    else:
        print('ERRO. Tente novamente.')

print('ENCERRADO')

