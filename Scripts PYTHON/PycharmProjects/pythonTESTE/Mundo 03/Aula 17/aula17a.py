num = [2, 5, 9, 1]
num[2] = 3 #altera o valor do indice indicado. LISTAS SÃO MÚTAVEIS
num.append(7) #adiciona o valor a ser adicionado a lista/ será adicionado no final
num.sort(reverse=True) #ordena de forma decrescente / para crescente limpar os parenteses()
num.insert(2, 2) #adiciona na posição indicada (2) o item (0)
print(f'Está lista tem {len(num)} elementos') #lenght = indica a quantidade de itens na lista
print(num)