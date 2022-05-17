nome = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer {}!'.format(nome))
nome = nome.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))  # ultimo valor do grupo formado no split
