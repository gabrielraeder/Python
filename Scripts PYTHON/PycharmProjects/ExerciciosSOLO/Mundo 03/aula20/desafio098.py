from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo - (passo + passo)
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio} ', end='-> ')
            inicio = inicio + passo
            sleep(.1)
    else:
        while inicio >= fim:
            print(f'{inicio} ', end='-> ')
            inicio = inicio - passo
            sleep(.1)

    print(' FIM!')



contador(1, 10, 1)
contador(10, 0, 2)
print()
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('INÍCIO: '))
b = int(input('FIM: '))
p = int(input('PASSO: '))
contador(a, b, p)
