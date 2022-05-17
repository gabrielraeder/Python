tup = ('caderno', 'cadeira', 'monitor', 'dermatologista', 'otorrinolaringologista', 'diamante')
for c in tup:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
