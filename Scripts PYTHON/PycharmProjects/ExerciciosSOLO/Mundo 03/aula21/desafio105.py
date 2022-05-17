def notas(n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando sedeve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    dic['total'] = len(n)
    maior = menor = 0
    for c in range(0, len(n)):
        if c == 0:
            maior = menor = n[c]
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
    dic['maior'] = maior
    dic['menor'] = menor
    media = sum(n) / len(n)
    dic['media'] = media
    if sit==True:
        if media >= 7:
            dic['situação'] = 'BOA'
        elif 5 < media < 7:
            dic['situação'] = 'RECUPERAÇÂO'
        else:
            dic['situação'] = 'RUIM'
    return dic


c = 1
list = list()
while True:
    nota = float(input(f'Digite a {c}ª nota: '))
    list.append(nota)
    c = c + 1
    while True:
        r = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
while True:
    op = str(input('Deseja mostrar a situação do aluno? [S/N] ')).strip().upper()[0]
    if r in 'SN':
        break
if op == 'S':
    resp = notas(list, sit=True)
else:
    resp = notas(list)
print(resp)
