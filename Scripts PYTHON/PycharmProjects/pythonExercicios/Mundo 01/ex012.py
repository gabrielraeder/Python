p = float(input('Qual é o preço do produto? R$'))
desc = p - (p*5/100)
print('O produto de valor {:.2f}, com desconto de 5% custará R${:.2f}'.format(p, desc))