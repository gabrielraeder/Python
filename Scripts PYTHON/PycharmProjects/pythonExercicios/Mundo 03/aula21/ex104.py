def leia(msg):
    ok = False
    # valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            # valor = int(n)
            n = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número válido\033[m')
        if ok:
            break
    return n #valor

n = leia('Digite um número: ')
print(f'Você acabou de digitar o número {n}')