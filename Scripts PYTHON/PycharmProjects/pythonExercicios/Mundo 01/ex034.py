from time import sleep
salario = float(input('Qual o salário do funcionário? R$ '))
if salario > 1250:
    novo = salario + salario*10/100
    print('Salário original: R$ {:.2f}'.format(salario))
    print('Novo salário com aumento de 10% = ', end='')
    sleep(2)
    print('R$ {:.2f}'.format(novo))
else:
    novo = salario + salario * 15 / 100
    print('Salário original: R$ {:.2f}'.format(salario))
    print('Novo salário com aumento de 15% = ', end='')
    sleep(2)
    print('R$ {:.2f}'.format(novo))