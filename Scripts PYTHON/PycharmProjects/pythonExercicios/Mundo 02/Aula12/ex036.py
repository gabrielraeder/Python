print('#='*10)
print('#'*3, '\033[1;33;40mEMPRÉSTIMOS\033[m', '#'*3)
print('#='*10)
print('')
v = float(input('Qual o valor do imóvel? R$ '))
s = float(input('Qual o seu salário? R$ '))
ano = int(input('Em quantos anos deseja pagar? '))
mensal = v / (ano*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação mensal será de R${:.2f}.'.format(v, ano, mensal))
if mensal > s*30/100:
    print('Empréstimo \033[1;97;41mNEGADO\033[m. A parcela R${:.2f} é superior a 30% de seu salário de R${:.2f}.'.format(mensal, s))
else:
    print('Empréstimo \033[1;97;42mAPROVADO!\033[m')