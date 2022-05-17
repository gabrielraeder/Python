def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2

def aumento(n=0, p=0):
    a = n * (p+100) / 100
    return a

def diminui(n=0, p=0):
    d = n * (100 - p) / 100
    return d

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

