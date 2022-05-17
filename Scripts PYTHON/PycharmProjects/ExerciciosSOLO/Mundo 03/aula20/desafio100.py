from random import randint

def sorteia(lst):
    for c in range(0, 5):
        num = randint(1, 10)
        lst.append(num)
    print(f'Sorteando 5 valores da lista: ', end='')
    for v in lst:
        print(f'{v}', end=', ')
    print('PRONTO!')
def somaPar(lst):
    soma = 0
    for item in lst:
        if item % 2 == 0:
            soma = soma + item
    print(f'Somando os valores pares de {lst}, temos {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
