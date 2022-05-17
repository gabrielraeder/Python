pos = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
mat = []
dado = []
par = []
for c in range(0, 9):
    n = (int(input(f'Digite um valor para {pos[c]}: ')))
    if n % 2 == 0:
        par.append(n)
    dado.append(n)
    mat.append(dado[:])
    dado.clear()

print(f' {mat[0]}   {mat[1]}   {mat[2]} \n'
      f' {mat[3]}   {mat[4]}   {mat[5]} \n'
      f' {mat[6]}   {mat[7]}   {mat[8]} ')
print()
soma3c = somapar = soma2l = 0
for item in par:
    somapar = item + somapar
s3c = mat[2] + mat[5] + mat[8]
total3 = 0
for item in s3c:
    total3 = total3 + item
s2l = mat[3] + mat[4] + mat[5]
maior2 = 0
for item in s2l:
    if item > maior2:
        maior2 = item
print(f'Soma dos pares = {somapar}\n'
      f'Soma terceira coluna = {total3}\n'
      f'Maior valor segunda linha = {maior2}')


