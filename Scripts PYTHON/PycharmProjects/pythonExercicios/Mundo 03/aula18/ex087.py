matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = mai = scol = 0
for l in range(0, 3):                   #LINHA            #'FOR' para linha e coluna para alimentar a lista
    for c in range(0, 3):               #COLUNA
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('#'*25)
for l in range(0, 3):                   #'FOR' para print dos resultados organizadamente
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:
            sp = sp + matriz[l][c]
    print()                             #a cada fim de c(coluna) ele pulará uma linha
print('#'*30)
print(f'A soma dos valores pares é {sp}.')
for l in range(0, 3):
    scol = scol + matriz[l][2]
print(f'A soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
print('#'*30)
