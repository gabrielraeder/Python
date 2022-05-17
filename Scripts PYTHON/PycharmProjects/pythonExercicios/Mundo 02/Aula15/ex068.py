from random import randint
cont = 0

while True:
    op = ' '
    while op not in 'PI':
        op = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    j = int(input('Número de 1 a 5: '))
    pc = randint(1, 5)
    total = pc + j
    print(f'O computador jogou {pc} e a soma foi {total}.')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if total % 2 == 0:
        if op == 'P':
            print('Você VENCEU! Vamos novamente...')
            cont = cont + 1
        elif op == 'I':
            break
    if total %2 != 0:
        if op == 'I':
            print('Você VENCEU! Vamos novamente...')
            cont = cont + 1
        elif op == 'P':
            break
print(f'Acabou! Você conquistou {cont} vitórias seguidas.')
