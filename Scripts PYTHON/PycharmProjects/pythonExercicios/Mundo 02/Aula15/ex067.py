print('+'*40)
while True:
    n = int(input('Digite um valor para ver sua tabuada: '))
    print('+' * 40)
    if n < 0:
        break
    for c in range(1,11):
        result = n * c
        print(f'{n} x {c:2} = {result}')
    print('+' * 40)
print('PROGRAMA ENCERRADO')