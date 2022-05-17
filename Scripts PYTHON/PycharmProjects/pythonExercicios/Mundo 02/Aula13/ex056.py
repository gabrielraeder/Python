somaidade = 0
print('='*29)
maiorhomem = 0
nomevelho = ''
totfem20 = 0
for p in range(1, 5):
    print('========= {}ª PESSOA ========='.format(p))
    nome = str(input('  Nome: ')).strip().capitalize()
    idade = int(input('  Idade: '))
    sexo = str(input('  Sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade
    if p == 1 and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totfem20 = totfem20 + 1
media = somaidade / 4
print('Média de idade do grupo é {} anos.'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maiorhomem, nomevelho))
print('Total de {} mulheres abaixo de 20 anos.'.format(totfem20))
