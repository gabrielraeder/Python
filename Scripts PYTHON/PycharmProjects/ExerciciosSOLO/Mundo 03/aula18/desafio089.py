lista = []
nomenota = []
notas = []
while True:
    soma = 0
    media = 0
    nome = str(input('NOME: ')).strip().capitalize()
    for n in range(0, 2):
        cont = 0
        while cont < 2:
            nota = float(input(f'{n+1}ª NOTA: '))
            if nota <= 10:
                soma = soma + nota
                notas.append(nota)
                cont = cont + 1
                break
            else:
                print('ERRO --> ', end=' ')
    media = soma /2
    nomenota.append(nome)
    nomenota.append(media)
    nomenota.append(notas[:])
    lista.append(nomenota[:])
    nomenota.clear()
    notas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('#'*30)
print('No. NOME          MÉDIA')
print('~'*30)
for i in range(0, len(lista)):
        print(f'{i+1} - {lista[i][0]: <15}', end='')
        print(f'{lista[i][1]:.1f}')
print('~'*30)
while True:
    op = int(input('Mostrar notas de qual aluno? (999 FINALIZAR) '))
    if op <= len(lista):
        print(f'Notas de {lista[op-1][0]} são {lista[op-1][2]}')
        print('~' * 30)
    if op > len(lista) and op != 999:
        print('ERRO. Tente novamente..')
    if op == 999:
        break
print('#'*30)
print('ENCERRADO')