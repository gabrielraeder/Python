a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a  # verificando o maior valor
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a  # verificando o menor valor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))
