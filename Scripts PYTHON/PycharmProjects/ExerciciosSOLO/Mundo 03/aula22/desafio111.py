from utilidades import moeda

valor = float(input('Digite um preço: R$ '))
aum = int(input('Aumento de quantos porcento? '))
red = int(input('Redução de quantos porcento? '))
moeda.resumo(valor, aum, red)
