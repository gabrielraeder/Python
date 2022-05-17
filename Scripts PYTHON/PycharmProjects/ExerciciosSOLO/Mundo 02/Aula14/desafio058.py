from random import randrange
n = randrange(0, 11)
erro = 0

j = int(input('Digite um valor entre 0 e 11: '))
while n != j:
    j = (int(input('ERROU! Tente novamente: ')))
    erro = erro + 1
print('ACERTOU! Os valores {} e {} são iguais!'.format(n, j))
print('Foram {} palpites.'.format(erro + 1))