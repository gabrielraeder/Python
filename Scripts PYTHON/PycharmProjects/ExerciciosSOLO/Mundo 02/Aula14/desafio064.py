n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um valor: '))
    s = s + n
    cont = cont + 1
    print('[999] ENCERRAR', end=' -- ')
print('Foram digitados {} valores.\nA soma de todos é {}.'.format(cont-1, s-999))