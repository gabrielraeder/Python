m18 = homens = m20 = 0
while True:
    print('-'*40)
    print('{:-^40}'.format('CADASTRE UMA PESSOA'))
    print('-' * 40)
    idade = int(input('IDADE: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('SEXO: [M/F] ')).strip().upper()[0]
    print('-' * 40)
    if idade >= 18:
        m18 = m18 + 1
    if sex == 'M':
        homens = homens + 1
    if sex == 'F' and idade < 20:
        m20 = m20 + 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        print('-' * 40)
        break
print(f'Maiores de 18 anos = {m18}\nHomens = {homens}\nMulheres com menos de 20 anos = {m20}')
