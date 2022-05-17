from ex108 import moeda


valor = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
aum = int(input('Aumento de quantos porcento? '))
print(f'Com aumento de {aum}%, temos {moeda.moeda(moeda.aumento(valor, aum))}.')
red = int(input('Redução de quantos porcento? '))
print(f'Com redução de {aum}%, temos {moeda.moeda(moeda.diminui(valor, red))}.')
