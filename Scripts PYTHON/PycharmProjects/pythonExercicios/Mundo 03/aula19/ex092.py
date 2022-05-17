from datetime import date
dados = dict()
dados['nome'] = str(input('NOME: ')).strip().capitalize()
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 = não possui): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('+'*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')
