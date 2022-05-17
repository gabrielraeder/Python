a = [2, 3, 4, 7]
'b = a'  #este comando faz as listas ficarem conectadas, isto é, alterar uma alterará a outra junto
b = a[:] #[:]FATIAMENTO, fará o B receber uma cópia dos valores de A / NÃO CRIA A LIGAÇÃO ENTRE AS LISTAS
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')