lista = []
c = 0
while True:
    print('=' * 50)
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('='*50)
print(f'Foram digitados {len(lista)} valores.')
print('-'*50)
print(f'Lista decrescente = {sorted(lista, reverse=True)}') # com este comando somente mostra organizado sem alterar a lista.
print('-'*50)
lista.sort(reverse=True) #com este comando altero a lista
if 5 in lista:
    print(f'O valor 5 está na lista na posição ', end='')
    for i in range(0, len(lista)): #ou usar -> for i, v in enumerate(lista:
        if lista[i] == 5:                         # if v == 5:
            print(f'{i}', end='.. ')
else:
    print('O valor 5 não se encontra.')
print()
print('=' * 50)
