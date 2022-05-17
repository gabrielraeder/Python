galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('NOME: ')).strip().capitalize())
    dado.append(int(input('IDADE: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print(dado)

for p in galera:
    if p[1] >=18:
        print(f'{p[0]} é maior de idade.')
        totmai = totmai + 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen = totmen + 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')