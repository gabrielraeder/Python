cont = 0
for c in range(0, 51):
    if c % 2 == 0 and c != 0:
        print(c, end=' ')
        cont = cont + 1
print('\n')
print(cont)


#ou
#for c in range(2, 51, 2):   está opção ocupa menos memória pois tem menor nº de ITERAÇÔES
    #print(c, end='-')