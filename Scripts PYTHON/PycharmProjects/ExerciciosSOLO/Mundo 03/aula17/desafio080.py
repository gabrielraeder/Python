lista = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  #lista[-1] = isto significa o ultimo item da lista. -1 referencia o primeiro de tras pra frente
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):

            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos+1} da lista')
                break
            pos = pos + 1
print(lista)