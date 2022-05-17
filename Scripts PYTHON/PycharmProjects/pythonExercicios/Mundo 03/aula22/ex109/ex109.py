import moeda

n = float(input('Preço do produto: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'O aumento de 10% é {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(n, 15, True)}')