valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont+1}º valor: ')))
#for v in valores:
for c, v in enumerate(valores):
    print(f'Na posição {c} o valor é {v}...')
print('FIM DA LISTA')