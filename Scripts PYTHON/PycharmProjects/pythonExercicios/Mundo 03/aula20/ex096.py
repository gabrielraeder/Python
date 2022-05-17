def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}mx{comp}m é de {a}m2.')


print(' Controle de terrenos ')
print('-'*21)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)