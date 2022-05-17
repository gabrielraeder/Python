from time import sleep


def contador(i, f, p):
    if p < 0:
        p = p *(-1)
    if p == 0:
        p = 1
    print('-='*20)
    print(f'contagem de {i} até o {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' -> ')
            sleep(.25)
            cont = cont + p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' -> ')
            sleep(.25)
            cont = cont - p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez!')
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fim, pas)