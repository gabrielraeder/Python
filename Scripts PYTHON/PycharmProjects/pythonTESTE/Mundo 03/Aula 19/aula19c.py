estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do estado: ')).upper()
    brasil.append(estado.copy())  #comando similar ao [:] das listas. No dicionario para copiar o conteudo somente funciona este .copy
print()
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}.')
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()