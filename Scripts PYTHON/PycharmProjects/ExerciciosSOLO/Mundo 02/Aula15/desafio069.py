m20 = 0
tot18 = 0
homens = 0
continuar = 'a'
print('#'*30)
while True:
    idade = int(input('Informe a idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('#' * 30)
    if idade > 18:
        tot18 = tot18 + 1
    if sex in 'M':
        homens = homens + 1
    if idade < 20 and sex in 'F':
        m20 = m20 + 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('#' * 30)
    if continuar in 'N':
        break
print(f'Maiores de 18 anos = {tot18}\nTotal de homens = {homens}\nMulheres abaixo de 20 anos = {m20}')
