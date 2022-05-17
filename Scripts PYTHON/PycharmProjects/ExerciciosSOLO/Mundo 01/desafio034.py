n = float(input('Informe o salário do funcionário: R$'))
if n > 1250.00:
    v = n*110/100
    print('Com aumento de 10% o salário agora será R${:.2f}.'.format(v))
else:
    v = n*115/100
    print('Com aumento de 15% o salário agora será R${:.2f}.'.format(v))
