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
print('='*33)
print(dic)
print('='*33)
print(f'O jogador {dic["nome"]} jogou {x} partidas.')
for c in range(0, len(dic['gols'])):
    print(f' => Na {c+1}ª partida, fez {dic["gols"][c]} gols.')
print(f'Foi um total de {dic["total"]} gols.')
print('='*33)