from time import sleep
salario = float(input('Qual o salário do funcionário? R$ '))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    porcento = 10
else:
    novo = salario + (salario * 15 / 100)
    porcento = 15
print('Salário original: R$ {:.2f}'.format(salario))
print('Novo salário com aumento de {}% = '.format(porcento), end='')
sleep(2)
print('R$ {:.2f}'.format(novo))