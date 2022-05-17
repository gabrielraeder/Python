lista = ('Aprender', 'lanche', 'exemplo', 'tupla', 'possivel',
         'munhequeira', 'pano', 'remedio', 'escorpiao', 'celular')
for c in lista:                         # retirou cada item da tupla para analise separado
    print(f'\nNa palavra {c.upper()} temos as vogais ', end='')
    for letra in c:                 # separou cada letra de cada item, que foi separado no FOR anterior, para analise
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
print(' ')
