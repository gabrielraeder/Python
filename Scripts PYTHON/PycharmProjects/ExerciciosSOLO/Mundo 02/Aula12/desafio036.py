print('-'*5, '\033[1;30;107mEMPRÉSTIMOS BANCÁRIO\033[m', '-'*5)
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
ano = int(input('Em quantos anos será pago o imóvel? '))
prestm = valor / (ano*12)
if prestm >= salario*30 / 100:
        print('Seu empréstimo foi negado.')
else:
        print('O empréstimo foi aprovado com prestação mensal de R${:.2f}!'.format(prestm))

print('-'*10, '\033[1;30;107mFIM\033[m','-'*10)


#salario < salario*70 / 100: