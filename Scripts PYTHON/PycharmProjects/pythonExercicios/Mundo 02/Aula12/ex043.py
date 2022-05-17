print('-='*20)
print('       Índice de Massa Corporal')
print('-='*20)
peso = float(input('Informe seu peso, em kg: '))
altura = float(input('Informe sua altura, em cm: '))
alt = altura / 100
imc = peso / (alt**2)
print('Seu IMC é de {:.2f} e você está '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO ideal.')
elif imc >=18.5 and imc < 25:
    print('no seu PESO IDEAL. Parabéns!')
elif imc >= 25 and imc < 30:
    print('com SOBREPESO. Cuide-se.')
elif imc >= 30 and imc < 40:
    print('OBESO. Cuide-se!')
elif imc >= 40:
    print('com OBESIDADE MÓRBIDA! Procure ajuda urgentemente!')
