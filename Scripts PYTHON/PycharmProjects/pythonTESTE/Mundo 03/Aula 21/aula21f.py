def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f
print('~'*35)
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print('~'*35)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')
print('~'*35)