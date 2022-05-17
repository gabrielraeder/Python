print('---TABUADA---')
n = int(input('Escolha um número: '))
for c in range(1, 11):
    print('   {} x {:2} = {:2}'.format(n, c, n*c))
