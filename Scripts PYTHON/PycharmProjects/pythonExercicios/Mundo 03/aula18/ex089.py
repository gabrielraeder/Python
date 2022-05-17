ficha = list()
while True:
    nome = str(input('NOME: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('#'*30)
print(f' {"no.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('~'*30)
for i, a in enumerate(ficha):
    print(f' {i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
print('~' * 30)
while True:
    op = int(input('Mostrar notas de qual aluno? (999) INTERROMPE: '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(ficha):
        print(f'Notas de {ficha[op-1][0]} são {ficha[op-1][1]}')

