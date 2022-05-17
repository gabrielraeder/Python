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

