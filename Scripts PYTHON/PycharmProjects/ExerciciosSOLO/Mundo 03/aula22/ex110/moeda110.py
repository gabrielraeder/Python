def metade(n=0, f=False):
    met = n / 2
    if f:
        return moeda(met)
    else:
        return met


def dobro(n=0, f=False):
    dob = n * 2
    if f:
        return moeda(dob)
    else:
        return n * 2


def aumento(n=0, p=0, f=False):
    a = n * (p+100) / 100
    if f:
        return moeda(a)
    else:
        return a


def diminui(n=0, p=0, f=False):
    d = n * (100 - p) / 100
    if f:
        return moeda(d)
    else:
        return d


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


def resumo(p, aum, red):
    print('-'*30)
    print(f'{" RESUMO DO VALOR ":^30}')
    print('-' * 30)
    print(f'Preço analisado:   {moeda(p)}')
    print(f'Dobro do Preço:    {dobro(p, f=True)}')
    print(f'Metado do preço:   {metade(p, f=True)}')
    print(f'{aum}% de aumento:    {aumento(p, aum, f=True)}')
    print(f'{red}% de redução:    {diminui(p, red, f=True)}')
    print('-' * 30)