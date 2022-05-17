from datetime import date
hj = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('ano de nascimento {}ª pessoa: '.format(c)))
    idade = hj - ano
    if idade >=18:
        maior = maior + 1
    else:
        menor = menor + 1
print('\033[1;30;42mMAIOR DE 18 ANOS = {}\033[m\n\033[1;30;41mMENOR DE 18 ANOS = {}\033[m'.format(maior, menor))
