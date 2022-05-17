from random import randrange
n1 = int(input('Tente descobrir o numero entre 0 e 5: '))
n2 = randrange(6)
print('O numero seleciona foi {}.'.format(n2))
if n1 == n2:
    print('Você acertou!')
else:
    print('Você errou.')
