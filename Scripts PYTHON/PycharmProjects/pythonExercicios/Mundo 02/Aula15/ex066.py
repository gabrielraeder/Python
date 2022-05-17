cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont = cont + 1
    s = s + n
    print('[999] ENCERRAR')
print(f'foram digitados {cont} números e a soma destes é {s}.')
