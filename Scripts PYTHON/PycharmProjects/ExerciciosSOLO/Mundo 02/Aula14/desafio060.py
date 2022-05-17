n = int(input('Digite um número: '))
c = n
fact = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fact = fact * c
    c = c - 1
print(fact)

print('\nFIM')