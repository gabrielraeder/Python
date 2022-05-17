n = float(input('Informe a velocidade do veículo: '))
if n > 80:
    print('MULTADO! Limite de velocidade permitida de 80km/h excedido!')
    multa = (n-80) * 7
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
