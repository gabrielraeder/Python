time = list()
jog = {}
partidas = list()
while True:
    jog.clear()
    jog['nome'] = str(input('NOME: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' --> Quantos gols na {c+1}ª partida? ')))
    jog['gols'] = partidas[:]
    jog['total'] = sum(partidas)
    time.append(jog.copy())
    while True:
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO!')
    if resp == 'N':
        break
print('=+'*31)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('=+'*31)
for k, v in enumerate(time):
    print(f'{k+1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=+'*31)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    busca = busca - 1
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca+1}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' -> no {i+1}º jogo, fez {g} gols.')
    print('-'*31)
print('ENCERRADO')






