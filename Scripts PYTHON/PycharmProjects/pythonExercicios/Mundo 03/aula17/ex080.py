lista = []
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Valor {n} adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor {n} adiciona na {pos+1}ª posição.')
                break
            pos = pos + 1
print(f'Os valores digitados foram {lista}')