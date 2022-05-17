from random import choice
print('$'*5, '\033[7;33mJOKENPÔ\033[m', '$'*5)
print()
j = str(input('Pedra, papel ou tesoura? ')).strip().upper()
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('Você escolheu {} e o computador {}.'.format(j, pc))
if pc == j:
    print('EMPATE')
elif pc == 'PEDRA' and j == 'TESOURA' or pc == 'PAPEL' and j == 'PEDRA' or pc == 'TESOURA' and j == 'PAPEL':
    print('Você PERDEU. =(')
else:
    print('Você GANHOU! PARABÉNS!!')
