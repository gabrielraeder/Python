n = int(input('informe o 1º termo: '))
r = int(input('Informe a razão da P.A.: '))
termo = n
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -'.format(termo), end=' ')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    print('=' * 20)
    mais = int(input('Quantos termos a mais você deseja: '))
print('='*20)
print('Foram exibidos {} termos.'.format(total))
print('='*20)
print('PROGRAMA ENCERRADO')

