import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
print('O aluno escolhido foi {}'.format(random.choice([a1, a2, a3, a4])))
