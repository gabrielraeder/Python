def ficha(nome, gol=0):
    if n == '':
        nome = '<DESCONHECIDO>'
    print(f'O Jogador {nome} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip().capitalize()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
