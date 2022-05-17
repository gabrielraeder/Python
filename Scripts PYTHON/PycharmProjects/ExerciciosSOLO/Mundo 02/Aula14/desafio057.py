sex = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('INVÁLIDO! Informe novamente [M/F] ')).strip().upper()[0]
print(sex)
print('FIM')
