tupla = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = 15
while n >= 10 or n < 0:
    n = int(input('Número entre 0 e 10: '))
    if n > 10 or n < 0:
        print('Tente novamente')
print(f'O número {n} por extenso é {tupla[n]}.')
