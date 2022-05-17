from random import randint
from time import sleep
print('\033[1;33m-=-\033[m'*24)
print('\033[1;36m        Vou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m'*24)
n1 = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
n2 = randint(0, 5) #randint escolhe m numero randomico entre os valores. Choice escolhe um dentre os valores informados.
print('PROCESSANDO...')
sleep(1)
if n1 != n2:
    print('Você errou! Meu número foi {}.'.format(n2))
else:
    print('Meu número também foi {}! Parabéns!'.format(n1))
print('')
print('\033[1;33m-=-\033[m'*11, '\033[1;36mFIM\033[m', '\033[1;33m-=-\033[m'*11)
