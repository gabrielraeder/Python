s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: #FLAG = 999
        break
    s = s + n
    cont = cont + 1
print(f'Foram digitados {cont} e a soma destes é {s}.')
