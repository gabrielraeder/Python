from random import randint
from time import sleep
itens = ('nada', 'PEDRA', 'PAPEL', 'TESOURA')
print('\033[4;30;42m{:=^50}\033[m'.format(' JOKENPÔ '))
jogador = int(input('''Jokenpô:
[1] PEDRA
[2] PAPEL
[3] TESOURA
Qual é a sua jogada? '''))
pc = (randint(1, 3))
print('JOO..')
sleep(1)
print('KEEN...')
sleep(1)
print('PÔÔÔÔ!!!')
print('-='*15)
print('O computador escolheu {}\n     Você escolheu {}'.format(itens[pc], itens[jogador]))
print('-='*15)
if pc == 1: # PC jogou PEDRA
    if jogador == 1:
        print('\033[1;30;107m {:-^28} \033[m'.format('EMPATE'))
    elif jogador == 2:
        print('\033[1;97;42m {:-^28} \033[m'.format('JOGADOR VENCEU! PARABÉNS!!'))
    elif jogador == 3:
        print('\033[1;97;41m {:-^28} \033[m'.format('COMPUTADOR VENCEU'))
    else:
        print('JOGADA INVÁLIDA')

elif pc == 2: #PC jogou PAPEL
    if jogador == 1:
        print('\033[1;97;41m {:-^28} \033[m'.format('COMPUTADOR VENCEU'))
    elif jogador == 2:
        print('\033[1;30;107m {:-^28} \033[m'.format('EMPATE'))
    elif jogador == 3:
        print('\033[1;97;42m {:-^28} \033[m'.format('JOGADOR VENCEU! PARABÉNS!!'))
    else:
        print('JOGADA INVÁLIDA')
elif pc == 3: # PC jogou TESOURA
    if jogador == 1:
        print('\033[1;97;42m {:-^28} \033[m'.format('JOGADOR VENCEU! PARABÉNS!!'))
    elif jogador == 2:
        print('\033[1;97;41m {:-^28} \033[m'.format('COMPUTADOR VENCEU'))
    elif jogador == 3:
        print('\033[1;30;107m {:-^28} \033[m'.format('EMPATE'))
    else:
        print('JOGADA INVÁLIDA')
print('-=' * 15)
