print('+'*8, '\033[0;35mDESAFIO 043\033[m', '+'*8)
print('')
a = float(input('Informe sua altura em cm: '))
p = float(input('Informe seu peso em kg: '))
imc = p / ((a/100)**2)
print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal. PARABÉNS!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está OBESO.')
else:
    print('Você está com OBESIDADE MÓRBIDA! Procure ajuda!')
print('')
print('+'*12, '\033[0;35mFIM\033[m', '+'*12)
