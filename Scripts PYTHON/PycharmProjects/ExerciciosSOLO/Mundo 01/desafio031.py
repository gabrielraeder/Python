n = float(input('Informa a distãncia da viagem: '))
if n <= 200:
    valor1 = n * 0.5
    print('O valor da viagem de {}km será R${:.2f}.'.format(n, valor1))
else:
    valor2 = n * 0.45
    print('Pvaçpr da voage, de {}km será R${:.2f}.'.format(n, valor2))