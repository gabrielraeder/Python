def maior(*num):
    print('-='*30)
    mai = 0
    for c in range(0, len(num)):
        if c == 0 or num[c] > mai:
            mai = num[c]
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
