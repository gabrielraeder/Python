n = 0
s = 0
cont = 0
maior = 0
menor = 99999999999
op = 'S'
while op not in 'N':
    if op == 'S':
        n = int(input('Digite um valor: '))
    cont = cont + 1
    s = s + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    op = str(input('Quer continuar? [S/N] ')).strip().upper()
media = s / cont
print('MÉDIA = {}'.format(media))
print('MAIOR = {}\nMENOR = {}'.format(maior, menor))