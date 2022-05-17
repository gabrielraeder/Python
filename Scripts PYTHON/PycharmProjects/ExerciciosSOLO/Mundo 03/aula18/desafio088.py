from random import randint
from time import sleep
lista = []
jogo = []

print('-'*35)
print(f'{" MEGA - SENA ":-^35}')
print('-'*35)
nj = int(input('Quantos jogos deseja? '))
for n in range(0, nj):
    for q in range(0, 6):
        j = 0
        while j < 6:
            rand = (randint(1, 60))
            if rand not in jogo:
                jogo.append(rand)
                j = j + 1
                break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
print(f'{f" Sorteando {nj} Jogos ":=^35}')

for i, v in enumerate(lista):
    print(f'Jogo {i+1}: {v}')
    sleep(.5)
