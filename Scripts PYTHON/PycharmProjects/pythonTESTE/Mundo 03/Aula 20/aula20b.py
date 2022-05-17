def contador(*num):
    tam = len(num)
    print(f'Recebi {num} e ao todo temos {tam} números.')
    for valor in num:
        print(valor, end=' ')
    print('FIM!')


contador(2, 1, 7)  #criará TUPLAS
contador(9, 0)
contador(4, 4, 7, 6, 2)