n = int(input('Digite um valor: '))
op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
cont = 1
soma = n
maior = n
menor = n
while op in 'S':
    n = int(input('Digite outro valor: '))
    soma = soma + n
    cont = cont + 1
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('MÉDIA = {:.2f}'.format(soma/cont))
print('MAIOR = {}\nMENOR = {}'.format(maior, menor))
