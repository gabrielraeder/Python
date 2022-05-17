from ex109 import moeda109


valor = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda109.moeda(valor)} é {moeda109.metade(valor, f=True)}')
print(f'O dobro de {moeda109.moeda(valor)} é {moeda109.dobro(valor, f=True)}')
aum = int(input('Aumento de quantos porcento? '))
print(f'Com aumento de {aum}%, temos {moeda109.aumento(valor, aum, f=True)}')
red = int(input('Redução de quantos porcento? '))
print(f'Com redução de {aum}%, temos {moeda109.diminui(valor, red, f=True)}')