def contador(i, f, p):
    """ ->  Faz uma contagem e mostra na tela
    :param i: INICIO da contagem
    :param f: FIM da contagem
    :param p: PASSO da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c = c + p
    print('FIM')


help(contador)