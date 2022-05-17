n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    op = int(input('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    >>>> Qual é a sua opção? '''))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
    elif op == 3:
        if n1 > n2:
            print('{} é o maior.'.format(n1))
        elif n1 < n2:
            print('{} é o maior.'.format(n2))
        else:
            print('Os valores são iguais.')
    elif op == 4:
        print('Informe novos números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op > 5:
        print('Opção inválida. Tente novamente.')
    print('-=='*10)
print(' PROGRAMA ENCERRADO')