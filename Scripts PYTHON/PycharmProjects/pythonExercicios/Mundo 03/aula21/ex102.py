def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: número a ser calculado
    :param show: (opcional) mostrar conta inteira
    :return: o resultado da fatorial do n.
    """
    print('-='*35)
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

        f = f * c
    return f


print(fatorial(5, show=True))