galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('NOME: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Tente novamente.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Tente novamente.')
    if resp == 'N':
        break
print('=+'*31)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade do grupo é {media:5.2f}.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] =='F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas acima da média de idade: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('ENCERRADO')
