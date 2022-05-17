from random import randint
from time import sleep
lista = list()
jogo = []
print('-'*40)
print(f'{"JOGO MEGA-SENA":^40}')
print('-'*40)
cont = 0
quant = int(input('Quantos jogos deseja? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-'*9, f' SORTEANDO {quant} JOGOS ', '-'*9)
for i , l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(.5)
print('-'*40)