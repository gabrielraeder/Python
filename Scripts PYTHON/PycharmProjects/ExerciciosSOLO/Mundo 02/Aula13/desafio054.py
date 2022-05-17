from datetime import date
hj = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = hj - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas são maiores de idade.\n{} ainda são de menor.'.format(maior, menor))



