'''num = [7, 5, 0, 3, 2, 1]
num.pop() #elimina o ultimo valor da lista
num.pop(2) #eliminará o item na posição 2
print(num)'''

num = [7, 5, 2, 3, 2, 1]
num.remove(2) #elimina o elemento indicado / caso este tenha repetido ele eliminará o primeiro encontrado somente
if 4 in num: #se tiver o valor 4 na lista
    num.remove(4) #removerá o valor 4
else:
    print('Não há numero 4.')
print(num)
print(f'Está lista tem {len(num)} elementos')