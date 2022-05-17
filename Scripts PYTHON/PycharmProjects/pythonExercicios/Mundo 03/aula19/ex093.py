jog = {}
partidas = list()
jog['nome'] = str(input('NOME: ')).strip().capitalize()
tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' --> Quantos gols na {c+1}ª partida? ')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)
print('=+'*31)
print(f'o jogador {jog["nome"]} jogou {len(jog["gols"])} partidas.')
for i, v in enumerate(jog['gols']):
    print(f'    => Na {i+1}ª partida, fez {v} gols.')
print(f'   {jog["nome"]} fez {jog["total"]} no total.')
