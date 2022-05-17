from ex107 import moeda


valor = float(input('Digite um preço: R$ '))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
aum = int(input('Aumento de quantos porcento? '))
print(f'Com aumento de {aum}%, temos {moeda.aumento(valor, aum)}')
red = int(input('Redução de quantos porcento? '))
print(f'Com redução de {aum}%, temos {moeda.diminui(valor, red)}')