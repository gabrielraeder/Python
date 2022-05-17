from datetime import date
dic = {}
dic['nome'] = str(input('NOME: ')).strip().capitalize()
ano = int(input('Ano de nascimento: '))
dic['idade'] = date.today().year - ano
dic['ctps'] = int(input('CTPS: '))

if dic['ctps'] != 0:
    dic['contrato'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salário: '))
    anoap = dic['contrato'] + 35
    anocontrato = (dic['contrato'] - ano) + 35

print(f'Nome: {dic["nome"]}\n'
      f'Idade: {dic["idade"]}\n'
      f'CTPS: {dic["ctps"]}')

if dic['ctps'] != 0:
    print(f'Contratado no ano: {dic["contrato"]}')
    print(f'Salário: R$ {dic["salario"]:.2f}')
    print(f'Se aposenta no ano {anoap} com {anocontrato} de idade')
