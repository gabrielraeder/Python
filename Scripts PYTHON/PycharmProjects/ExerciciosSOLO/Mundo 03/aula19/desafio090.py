dic = {}
dic['nome'] = str(input('NOME: ')).strip().capitalize()
dic['media'] = float(input('Média: '))
print(f'Nome é {dic["nome"]}')
print(f'A média é {dic["media"]}')
if dic['media'] >= 7:
    print('APROVADO')
else:
    print('REPROVADO')