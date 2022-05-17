print('-='*30)
s = 0
cont = 0
velho = 0
for c in range(1, 5):
    nome = str(input('Nome {}ª pessoa: '.format(c))).strip().capitalize()
    idade = int(input('Idade {}ª pessoa: '.format(c)))
    sexo = int(input('Sexo {}ª pessoa:\n[1] FEMININO\n[2] MASCULINO '.format(c)))
    print('-='*30)
    if idade > 0:
        s = s + idade
    if sexo == 1 and idade < 20:
        cont = cont + 1
    if c == 1:
        velho = idade
    else:
        if idade > velho:
            velho = idade
            n = nome
print('Média de idade do grupo é {:.0f}.'.format(s / 4))
print('Temos {} mulheres menores que 20 anos.'.format(cont))
print('A pessoa mais velha tem {} anos e seu nome é {}'.format(velho, n))

