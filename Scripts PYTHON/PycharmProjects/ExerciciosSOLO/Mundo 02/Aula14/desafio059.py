n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('='*18)
op = 0
maior = 0
while op != 5:
    op = int(input('''Opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa  ESCOLHA: '''))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
        print('=' * 15)
    if op == 2:
        print('{} x {} = {}'.format(n1, n2, (n1 * n2)))
        print('=' * 15)
    if op == 3:
        if n1 > n2:
            maior = maior + n1
            print('O maior valor é {}.'.format(maior))
            print('=' * 15)
        elif n1 < n2:
            maior = maior + n2
            print('O maior valor é {}.'.format(maior))
            print('=' * 15)
        else:
            print('Os valores são iguais.')
            print('=' * 15)
    if op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=' * 15)

print('========FIM========')
