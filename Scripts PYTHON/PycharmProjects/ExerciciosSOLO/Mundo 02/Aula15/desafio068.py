from random import choice
from random import randint
cont = 0
while True:
    j = str(input('Par ou ímpar? ')).strip().upper()
    if j not in 'PARIMPAR':
        print('OPÇÃO INVALIDA. Recomece.')
    else:
        n = int(input('Valor de 1 a 5: '))
        pc = randint(1, 5)
        if j == 'PAR':
            if (pc + n) % 2 == 0:
                print('Você VENCEU! Vamos jogar de novo!')
                cont = cont + 1
            else:
                print('Você PERDEU!')
                break
        elif j == 'IMPAR':
            if (pc + n) % 2 != 0:
                print('Você VENCEU! Vamos jogar de novo!')
                cont = cont + 1
            else:
                print('Você PERDEU!')
                break
if cont > 1:
    print(f'Você conseguiu {cont} vitórias seguidas.')
elif cont == 1:
    print('Você conseguiu somente 1 vitória seguida.')
else:
    print('ZERO vitórias!')
