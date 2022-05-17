from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados:')
rank = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.4)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('='*25)
print(f'{"RESULTADO":-^25}')
print('='*25)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
print('='*25)