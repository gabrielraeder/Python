dic = {}
lista = []
totidade = 0
while True:
    dic['nome'] = str(input('NOME: ')).strip().capitalize()
    dic['sexo'] = str(input('SEXO [M/F]: ')).strip().capitalize()[0]
    dic['idade'] = int(input('IDADE: '))
    totidade = totidade + dic['idade']
    lista.append(dic.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('CONTINUAR? [S/N]' )).strip().upper()[0]
    if op == 'N':
        break
print(lista)
print()
print(f'O grupo tem {len(lista)} pessoas.')
media = totidade / len(lista)
print(f'A média de idade é de {media} anos')
print('As mulheres cadastradas foram: ',end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print('Pessoas acima da média de idade: ', end='')
for c in lista:
    if c['idade'] > media:
        print(f'{c["nome"]}, {c["idade"]}')


