aluno = dict()
aluno['nome'] = str(input('NOME: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['sit'] = 'APROVADO'
elif 5<= aluno['media'] < 7:
    aluno['sit'] = 'Recuperação'
else:
    aluno['sit'] = 'REPROVADO'

print(f'Aluno {aluno["nome"]} teve média {aluno["media"]} e está {aluno["sit"]}')
print()
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')