import moeda

n = float(input('Preço do produto: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'O aumento de 10% é {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo 15%, temos {moeda.moeda(moeda.diminuir(n, 15))}')