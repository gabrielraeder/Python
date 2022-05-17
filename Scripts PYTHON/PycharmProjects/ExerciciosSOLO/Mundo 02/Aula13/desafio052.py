tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        tot = tot + 1
if tot == 2:
    print('Número PRIMO!')

