lanche = ('Burger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)): #len(lanche) = 5
    print(f'Eu vou comer {lanche[cont]} na posição {cont + 1}')
print('-'*40)
for comida in lanche:                   #deste formato não é possivel mostrar a posição
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')
print('-'*40)
for pos, comida in enumerate(lanche):             #enumerate permitirá mostrar posição
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba!')