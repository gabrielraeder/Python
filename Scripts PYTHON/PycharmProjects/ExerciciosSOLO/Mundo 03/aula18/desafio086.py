pos = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
mat = []
dado = []
for c in range(0, 9):
    n = (int(input(f'Digite um valor para {pos[c]}: ')))
    dado.append(n)
    mat.append(dado[:])
    dado.clear()
print(mat)
print(f' {mat[0]}   {mat[1]}   {mat[2]} \n'
      f' {mat[3]}   {mat[4]}   {mat[5]} \n'
      f' {mat[6]}   {mat[7]}   {mat[8]} ')
