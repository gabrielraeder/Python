teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #sem o [:] vinculará ao invés de copiar. Vinculado, ao mudar um item de uma lista a outra mudará tbm.
teste[0] = 'Ana'
teste[1] = 33
galera.append(teste[:])
teste[0] = 'Joaquim'
teste[1] = 13
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 45
galera.append(teste[:])
print(galera)
print(galera[0])
print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')