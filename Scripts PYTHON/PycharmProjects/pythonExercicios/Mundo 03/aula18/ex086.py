matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): #LINHA            #'FOR' para linha e coluna para alimentar a lista
    for c in range(0, 3): #COLUNA
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('#'*25)
for l in range(0, 3):           #'FOR' para print dos resultados organizadamente
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() #a cada fim de c(coluna) ele pulará uma linha
print('#'*25)