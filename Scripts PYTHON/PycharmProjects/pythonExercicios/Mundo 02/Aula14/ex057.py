sex = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]  #[] = fatiamento
while sex not in 'MF':
    sex = str(input('ERRO. Tente novamente.\n Qual é o seu sexo? [M/F] ' )).strip().upper()[0]
if sex in 'M':
    sex = 'MASCULINO'
elif sex in 'F':
    sex = 'FEMININO'
print(sex)