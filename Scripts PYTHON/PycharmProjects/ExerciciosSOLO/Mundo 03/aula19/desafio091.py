from random import randint
from operator import itemgetter
from time import sleep
dic = {}
lista = []
print('-'*25)
for c in range (1, 5):
    dic = {'jogador':f'Jogador{c}', 'valor':randint(1,6)}
    lista.append(dic.copy())
for k in range(0, len(lista)):
    print(f'o {lista[k]["jogador"]} tirou {lista[k]["valor"]} no dado')
    sleep(.5)
print('-'*25)
print('RANKING')
lista.sort(key=itemgetter('valor'), reverse=True)
for c in range(0, len(lista)):
    print(f'{c+1}º Lugar: {lista[c]["jogador"]} com {lista[c]["valor"]}')
print('-' * 25)