def fatorial(n, show=False):
    """
    CALCULA O FATORIAL DE UM NUMERO:
    :param n: o numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        f = f * c
        if show==True:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
    return f


n = int(input('Digite um número: '))
op = str(input('Deseja ver o calculo? [S/N] ')).strip().upper()[0]
if op == 'S':
    print(fatorial(n, True))
else:
    print(fatorial(n))
