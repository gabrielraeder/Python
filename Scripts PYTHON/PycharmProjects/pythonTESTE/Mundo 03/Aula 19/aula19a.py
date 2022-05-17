pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}     #dicionario {}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.values():
    print(k)
for k in pessoas.keys():
    print(k)
for k in pessoas.items():
    print(k)
print()
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

