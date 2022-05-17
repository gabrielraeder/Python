n = (int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
     int(input('Terceiro valor: ')), int(input('Quarto valor: ')))
print('#'*25)
print(f'O 9 apareceu {n.count(9)} vezes na tupla.')
print('#'*25)
if 3 in n:
    print(f'O 3 apareceu na {n.index(3)+1}ª posição.')
    print('#' * 25)
print('Os pares são: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
