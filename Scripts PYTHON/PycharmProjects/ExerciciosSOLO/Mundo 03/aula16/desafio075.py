num = (int(input('Primeiro valor: ')),
       int(input('Segundo valor: ')),
       int(input('Terceiro valor: ')),
       int(input('Quarto valor: ')))
print(f'Você digitou os valores {num}.')
print(f'O número 9 apareceu {num.count(9)}.')
if 3 in num:
    print(f'o primeiro número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os pares são ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=', ')
