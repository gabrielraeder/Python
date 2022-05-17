salario = float(input('Qual é o salário do funcionário? R$'))
aumento15 = salario + (salario*15/100)
print('O funcionário que ganhava R${:.2f}, com aumento de 15%, passará a receber R${:.2f}'.format(salario, aumento15))
