from time import sleep
while True:
    print('~' * 45)
    n = int(input('Informe um número para ver sua tabuada: '))
    print('~' * 45)
    if n < 0:
        break
    for c in range(1, 11):
        result = c * n
        print(f'{n} x {c} = {result}')
        sleep(.3)

    sleep(1)
print('PROGRAMA ENCERRADO')
