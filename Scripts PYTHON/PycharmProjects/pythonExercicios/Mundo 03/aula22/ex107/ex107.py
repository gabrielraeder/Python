import moeda

n = float(input('Preço do produto: R$ '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'O aumento de 10% é {moeda.aumentar(n, 10)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(n, 15)}')
